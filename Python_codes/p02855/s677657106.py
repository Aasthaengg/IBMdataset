def solve(h, w, k, s): 
    p = []
    for r in range(h):
        for c in range(w):
            if s[r][c] == "#":
                p.append((len(p)+1, r, c)) 
    p = sorted(p, key=lambda _:_[2])
    mask = [[0]*w for r in range(h)]
    for id, r, c in p:
        while c >= 0:
            if mask[r][c] == 0:
                mask[r][c] = id
            else:
                break
            c -= 1
    for id, r, c in p:
        c += 1
        while c < w:
            if mask[r][c] == 0:
                mask[r][c] = id
            else:
                break
            c += 1
    for sr in range(h):
        for sc in range(w):
            id = mask[sr][sc]
            r, c = sr-1, sc
            while r >= 0:
                if mask[r][c] == 0:
                    mask[r][c] = id
                else:
                    break
                r -= 1
    for sr in range(h):
        for sc in range(w):
            id = mask[sr][sc]
            r, c = sr+1, sc
            while r < h:
                if mask[r][c] == 0:
                    mask[r][c] = id
                else:
                    break
                r += 1
    for r in range(h):
        print(" ".join(map(str, mask[r])))

h, w, k = map(int, input().split())
s = [input() for r in range(h)]
solve(h, w, k, s)


