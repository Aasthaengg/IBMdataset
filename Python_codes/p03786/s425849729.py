n=int(input())
A=sorted(list(map(int,input().split())))
B=[A[0]]
for i in range(1,n):
  B.append(B[-1]+A[i])
ans=0
j=-1
for i in range(n-1):
  if B[i]*2<A[i+1]:
    ans=ans+i-j
    j=i
print(n-ans)