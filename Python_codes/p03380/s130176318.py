N=int(input())
l=list(map(int,input().split()))
A=max(l)
mid=(A//2)+1 if A%2!=0 else A//2
dis_min=float("Inf")
l.sort()
ans=1
for i in l:
   if dis_min>abs(i-mid):
      dis_min=abs(i-mid)
      ans=i
print(A,ans)