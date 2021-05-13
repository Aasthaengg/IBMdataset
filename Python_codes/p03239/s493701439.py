n,t = map(int,input().split())
c = []
for i in range(n):
    c1,t1 = map(int,input().split())
    if t1 <= t:
        c.insert(i,c1)
if len(c) == 0:
    print("TLE")
else:
    c.sort(key=int)
    print(c[0])