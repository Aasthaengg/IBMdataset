n=int(input())

A = list(map(int, input().split()))
l = [0] * len(A)

ans=0
m=A[0]

for i in A:
  if m>i:
    ans = ans +(m-i)
  
  else:
    m=i
  
print(ans)  
