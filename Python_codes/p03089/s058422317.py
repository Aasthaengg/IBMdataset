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

n = inn()
b = inl()
ans = []
for i in range(n):
    #ddprint(i)
    #ddprint(b)
    #ddprint(ans)
    for j in range(n-i-1,-1,-1):
        if b[j]==j+1:
            ans.append(j+1)
            for k in range(j,n-i-1):
                b[k] = b[k+1]
            break
    if len(ans)<i+1:
        print(-1)
        exit()
ans.reverse()
for x in ans:
    print(x)
