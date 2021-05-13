N=int(input())
s=list(map(int,input().split()))
z=0
for i in range(N):
  while s[i]%2==0:
    z+=1
    s[i]//=2
print(z)