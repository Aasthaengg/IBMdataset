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

s = ins()
k = inn()
n = len(s)
t = [ord(c)-ord('a') for c in s]
for i in range(n):
    if t[i]>0 and k>=26-t[i]:
        k -= 26-t[i]
        t[i] = 0
if k>0:
    t[n-1] = (t[n-1]+k)%26
print(''.join([chr(t[i]+ord('a')) for i in range(n)]))
