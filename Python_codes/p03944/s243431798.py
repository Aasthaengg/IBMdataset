import sys
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))  #空白あり

W,H,N = LI()

s,t,u,v = 0,W,0,H
for i in range(N):
    x,y,a = LI()
    if a == 1:
        s = max(s,x)
    if a == 2:
        t = min(t,x)
    if a == 3:
        u = max(u,y)
    if a == 4:
        v = min(v,y)

if t > s and v > u:
    print(max(0,(t-s)*(v-u)))
else:
    print(0)
