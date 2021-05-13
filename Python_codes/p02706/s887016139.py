n,m = (int(i) for i in input().split())
A = [int(i) for i in input().split()]
ans = n - sum(A)
if ans <= -2: print(-1)
else: print(ans)
