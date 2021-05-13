N=int(input())
A=list(map(int,input().split()))
mid=sum(A)/len(A)
b=float('inf')
for i,a in enumerate(A):
  sa=abs(mid-a)
  if(sa<b):
    b=sa
    res=i
print(res)