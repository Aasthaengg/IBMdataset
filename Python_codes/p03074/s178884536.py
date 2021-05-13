#from collections import deque,defaultdict
printn = lambda x: print(x,end='')
inn = lambda : int(input())
inl   = lambda: list(map(int, input().split()))
inm   = lambda:      map(int, input().split())
ins = lambda : input().strip()
DBG = True # and False
BIG = 10**18
R = 10**9 + 7

def ddprint(x):
  if DBG:
    print(x)

n,k = inm()
s = ins()
seq = []
strk = 0
for i in range(n):
    if i==0 or s[i-1]==s[i]:
        strk += 1
    else:
        seq.append(strk)
        strk = 1
seq.append(strk)
if len(seq)<=2*k:
    print(n)
    exit()
seq.extend([0]*8)
#ddprint(seq)
if s[0]=='0':
    mx = sm = sum(seq[:2*k])
    sm += seq[2*k]+seq[2*k+1]-seq[0]
    mx = max(mx,sm)
    stt = 1
    end = 2*k+1
else:
    mx = sm = sum(seq[:2*k+1])
    stt = 0
    end = 2*k
while end<len(seq)-4:
    sm += seq[end+1]+seq[end+2]-seq[stt]-seq[stt+1]
    stt += 2
    end += 2
    mx = max(mx,sm)
print(mx)
