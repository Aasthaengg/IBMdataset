N,M=map(int,input().split())
D=[]
for i in range(M):
  D.append(list(map(int,input().split())))
  D[-1]=D[-1][1:]
L=list(map(int,input().split()))
count=0
s=[]
for i in range(2**N):
  p = True
  for j in range(M):
    tmp = 0
    for k in range(N):
      if i>>k & 1:
        if k+1 in D[j]:
          tmp+=1
    if not L[j] == tmp%2:
      p = False
      break
  if p:
    s.append(bin(i))
    count+=1
print(count)