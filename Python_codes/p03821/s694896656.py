n=int(input())
L=[list(map(int,input().split())) for _ in range(n)][::-1]
c=0
for a,b in L:
  a+=c
  c+=(-a)%b
print(c)