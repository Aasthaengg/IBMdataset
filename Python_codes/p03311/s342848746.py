n=int(input())
a=list(map(int,input().split()))
b=[]
for i in range(n):
  b.append(a[i]-i-1)
b.sort()
c=b[n//2]
ans=100000000000000000000
for i in range(c-2,c+3):
  temp=0
  for j in range(n):
    temp+=abs(b[j]-i)
  if temp<ans:
    ans=temp
print(ans)