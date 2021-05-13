import itertools

def main():
    N = int(input())
    z = []
    ans = 51
    for i in range(N):
        z.append(tuple(map(int, input().split())))
    z.sort(key=lambda x: x[1])
    z.sort(key=lambda x: x[0], reverse=True)
    if len(z) == 1:
        print(1)
        return
    for i, j in itertools.combinations(range(N), 2):
        p = z[i][0] - z[j][0]
        q = z[i][1] - z[j][1]
        ans = min(ans, solve(N, z, p, q))
    print(ans)

def solve(N, z, p, q):
    passlist = set()
    cnt = 0
    for i in range(N):
        if z[i] in passlist:
            continue
        x, y = z[i][0], z[i][1]
        for j in range(N):
            s, t = x-p, y-q
            if (s, t) not in z:
                cnt += 1
                break
            passlist.add((s, t))
            x, y = s, t
    return cnt

if __name__ == "__main__":
    main()
