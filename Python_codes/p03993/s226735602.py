N = int(input())
A = list(map(int,input().split()))
a = 0
ans = 0

for i in A:
  a+=1
  if A[i-1]==a:
    ans+=1
  
  
print(ans//2)