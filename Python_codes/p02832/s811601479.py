N = int(input())
A = [int(i) for i in input().split()]

ans = 0
c = 1
for i in range(N):
    if A[i] == c:
        c += 1
    else:
        ans += 1

if c == 1:
    print(-1)
else:
    print(ans)
