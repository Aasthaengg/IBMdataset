n=int(input())
H=list(map(int,input().split()))
c=0
C=[]
h=H[0]
ans=0
for i in range(1,n):
  if H[i]<=h:
    c+=1
    h=H[i]
    ans=max(c,ans)
  if H[i]>h:
    c=0
    h=H[i]
    
print(ans)