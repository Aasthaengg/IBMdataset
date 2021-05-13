n,k=[int(input()) for i in range(2)]
X=list(map(int,input().split()))
ans = 0
for x in X:
  ans += min(2*x,2*(k-x))
print(ans)