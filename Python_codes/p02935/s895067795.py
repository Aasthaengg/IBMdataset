N = int(input())
A = sorted(list(map(int,input().split())))
ans = (A[0] + A[1]) / 2
for i in range(2, N):  ans = (ans + A[i]) / 2
print(ans)