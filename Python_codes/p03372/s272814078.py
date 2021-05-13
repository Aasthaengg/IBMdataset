N,C = map(int,(input().split()))
x = [0]*(N+1)
v = [0]*N
for i in range(N):
    x[i],v[i] = map(int,(input().split()))

sumv = [0]*(N+1)
for i in range(1,N+1):
    sumv[i] = sumv[i-1] + v[i-1]
csumv = [0]*(N+1)
for i in range(1,N+1):
    csumv[i] = csumv[i-1] + v[N-i]

sclo = [0]*(N+1)
for i in range(1,N+1):
    sclo[i] = sumv[i] - x[i-1]
scclo = [0]*(N+1)
for i in range(1,N+1):
    scclo[i] = csumv[i] - (C-x[N-i])

#print(sumv,sclo)
#print(csumv,scclo)

# まず反時計に行くとき
max_point = [0]*(N+1)
M = -1
for i in range(N+1):
    M = max(M,sclo[i])
    max_point[N-i] = M

point = [0]*(N+1)
for i in range(N+1):
    point[i] = scclo[i]-(C-x[N-i]) + max_point[i]

ans = max(point)

# まず時計に行くとき
max_point2 = [0]*(N+1)
M2 = -1
for i in range(N+1):
    M2 = max(M2,scclo[i])
    max_point2[N-i] = M2

point2 = [0]*(N+1)
x.insert(0,0)
for i in range(N+1):
    point2[i] = sclo[i]-(x[i]) + max_point2[i]

ans2 = max(point2)

ans3 = max(sclo)
ans4 = max(scclo)
print(max(ans,ans2,ans3,ans4))