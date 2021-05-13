import sys
input = sys.stdin.readline

S=list(input().rstrip('\n'))
N=len(S)
n = 'R'
change = []
for i in range(1,N):
  if S[i] != n:
    change.append(i)
    n = S[i]

now = 0
last = 0
res = [0]*N
for i in range(len(change)):
  if now==0:
    if i == len(change)-1:
      L=N-change[i]
    else:
      L = change[i+1]-change[i]
    R = change[i]-last
    if (L+R)%2==0:
      res[change[i]]=(L+R)//2
      res[change[i]-1]=(L+R)//2
    else:
      if L>R:
        if L%2==0:
          LR=1
        else:
          LR=0
      else:
        if R%2==0:
          LR=0
        else:
          LR=1
      if LR==0:
        res[change[i]]=(L+R+1)//2
        res[change[i]-1]=(L+R-1)//2
      else:
        res[change[i]]=(L+R-1)//2
        res[change[i]-1]=(L+R+1)//2
    now += 1
  else:
    last = change[i]
    now -= 1
print(*res)
