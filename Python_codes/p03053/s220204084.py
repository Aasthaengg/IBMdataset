from collections import deque
def solve():
    H,W = map(int,input().split())
    A = [list(input()) for _ in range(H)]

    q = deque()
    for h in range(H):
        for w in range(W):
            if A[h][w] == '#':
                q.append((h,w))
    
    q.append((-1,-1))
    ans = 0
    while len(q) > 0:
        h,w = q.popleft()
        if h == -1 and w == -1:
            if len(q) > 0:
                q.append((-1,-1))
                ans += 1
            continue

        d = ((0,1),(0,-1),(1,0),(-1,0))
        for dh, dw in d:
            if 0 <= h+dh < H and 0 <= w+dw < W and A[h+dh][w+dw] == '.':
                A[h+dh][w+dw] = '#'
                q.append((h+dh,w+dw))
    print(ans)

if __name__ == '__main__':
    solve()