n=int(input())
A=list(map(int,input().split()))
ans = [0]*(n+1)
for i in range(n):
  ans[i+1] = ans[i]+A[i]
prin = 10**100
for i in range(1,n):
  prin = min(prin,abs(ans[i]-(ans[n]-ans[i])))
print(prin)