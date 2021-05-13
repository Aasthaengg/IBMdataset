N = int(input())
A = list(map(int,input().split()))
ave = sum(A)/N
ans = 0
sa = 10**9
for i in range(N):
    x = max(A[i]-ave,ave-A[i])
    if x < sa:
        sa = x
        ans = i
print(ans)