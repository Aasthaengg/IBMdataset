n,k=map(int,input().split())
c=0
for b in range(k+1,n+1):
  c+=n//b*(b-k)+max(n%b-k+1,0)-(k<1)
print(c)