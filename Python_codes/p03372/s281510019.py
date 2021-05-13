import sys
input = lambda : sys.stdin.readline().rstrip()
sys.setrecursionlimit(max(1000, 10**9))
write = lambda x: sys.stdout.write(x+"\n")


# inputna
n,c = list(map(int, input().split()))
xv = [tuple(map(int, input().split())) for _ in range(n)]
c0 = []
c1 = []
v = 0
for i in range(n):
    v += xv[i][1]
    c0.append(v-xv[i][0])
v = 0
for i in range(n-1,-1,-1):
    v += xv[i][1]
    c1.append(v-(c-xv[i][0]))
c1 = c1[::-1]
d0 = []
d1 = []
v = 0
for i in range(n):
    v += xv[i][1]
    d0.append(v-2*xv[i][0])
v = 0
for i in range(n-1,-1,-1):
    v += xv[i][1]
    d1.append(v-2*(c-xv[i][0]))
d1 = d1[::-1]
# print(d0,d1)
for i in range(1,n):
    c0[i] = max(c0[i-1], c0[i])
    d0[i] = max(d0[i-1], d0[i])
for i in range(n-2, -1, -1):
    c1[i] = max(c1[i+1], c1[i])
    d1[i] = max(d1[i+1], d1[i])
m0 = max(c0)
m1 = max(c1)
if n>1:
    m2 = max((c0[i]+d1[i+1]) for i in range(n-1))
    m3 = max((c1[i]+d0[i-1]) for i in range(1,n))
else:
    m2 = m3 = -1
ans = max(m0,m1,m2,m3,0)
print(ans)