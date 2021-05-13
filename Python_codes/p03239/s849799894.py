N,T = map(int,input().split())
d =[]
for i in range(N):
    c,t = map(int,input().split())
    if t <= T:
        d.append(c)

d.sort()

if len(d) == 0:
    print("TLE")

else:
    print(d[0])
