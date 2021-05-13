N=int(input())
S=list(map(str,input().split()))
p=[]
for i in range(N):
  if not S[i] in p:
    p.append(S[i])
if len(p)==3:
  print('Three')
else:
  print('Four')