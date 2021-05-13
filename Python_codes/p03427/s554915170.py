N=list(input())
n=[int(i) for i in N]
L=len(N)
if L==1:
  print(n[0])
elif n[1:L]==[9]*(L-1):
  print(sum(n))
else:
  print((L-1)*9+n[0]-1)