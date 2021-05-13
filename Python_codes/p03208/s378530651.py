N,K = map(int,input().split())
arr = []

for i in range(N):
  a = int(input())
  arr.append(a)
  
arr.sort()
ans = 10**10

for i in range(N-K+1):
  a = arr[i]
  b = arr[i+K-1]
  c = b-a
  ans = min(ans,c)
  
print(ans)
