n=int(input())
a=list(map(int,input().split()))
ans=[0]*len(a)
c=a[0]
for i in range(1,n):
  c^=a[i]
for j in range(n):
  ans[j]=str(c^a[j])
print(" ".join(ans))