N=int(input())
A=list(map(int,input().split()))
S=sum(A)
minx=S
sum=0
for x in A:
  sum+=x
  minx=min(minx,abs(sum-(S-sum)))
print(minx)
