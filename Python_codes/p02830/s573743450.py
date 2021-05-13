N=int(input())
S,T=list(input().split())

L=''
for i in range(N):
  L+=S[i]
  L+=T[i]
print(L)