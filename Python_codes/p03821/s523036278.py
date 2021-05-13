N=int(input())
c=0
L=[list(map(int,input().split())) for _ in range(N)]
L=L[::-1]
for i in range(N):
  a,b=L[i]
  a+=c
  c+=b-(a%b)-(a%b==0)*b
print(c)