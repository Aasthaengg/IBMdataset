H, W = map(int, input().split())
N = int(input())
A = list(map(int, input().split()))

x = 0
for i in range(H):
    ans = []
    for j in range(W):
        ans.append(x+1)
        A[x] -= 1
        if A[x] == 0:
            x += 1
    if i % 2 == 0:
        print(*ans)
    else:
        print(*ans[::-1])