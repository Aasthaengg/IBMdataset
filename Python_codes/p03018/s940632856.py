from collections import deque

s=input()
s=s.replace("BC","D")
N=len(s)

cnt=0
cntA=0
cntD=0

for i in range(N):
  if s[i]=="A":
    cntA += 1
  elif s[i]=="D":
    cnt += cntA
  else:
    cntA=0
    cntD=0
    
print(cnt)