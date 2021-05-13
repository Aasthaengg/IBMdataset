def II(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))
def check(n):
  n=str(n)
  if len(n)!=N:
    return False
  for j in range(M):
    if n[int(S[j])]!=str(C[j]):
      return False
  return True  
N,M=MI()
S=[]
C=[]
for j in range(M):
  s,c=MI()
  s-=1         
  S.append(s)
  C.append(c)
i=0
while True:
  if check(i):
    print(i)
    exit()
  i+=1
  if i>1000:
    break  
print(-1)