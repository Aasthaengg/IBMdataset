N,C = map(int,input().split())
x1=[]
v1=[]

for i in range(N):
    x,v = map(int,input().split())
    x1.append(x)
    v1.append(v)
x2 = [C-x for x in x1]
v2 = [v for v in v1]
x2.reverse()
v2.reverse()

res1 = 0
res2 = 0
s1 = 0
s2 = 0
r1 = [0]
r2 = [0]
for i in range(N):
    s1 += v1[i]
    s2 += v2[i]
    res1 = max(res1,s1-x1[i])
    res2 = max(res2,s2-x2[i])
    r1.append(res1)
    r2.append(res2)

vl1 = [0]*(N+1)
vl2 = [0]*(N+1)
for i in range(N):
    vl1[i+1] = v2[i]+vl1[i]
    vl2[i+1] = v1[i]+vl2[i]
for i in range(N):
    vl1[i+1] -= 2*x2[i]
    vl2[i+1] -= 2*x1[i]



ans = 0
for i in range(N+1):
    res = vl1[i]+r1[N-i]
    if res > ans:
        ans = res
    res = vl2[i]+r2[N-i]
    if res > ans:
        ans = res

print(ans)