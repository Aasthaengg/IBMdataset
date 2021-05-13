N,T = map(int,input().split())
mn = 10**10
for i in range(N):
    c,t = map(int,input().split())
    #print(c,t)
    if t <= T and c <= mn:
        mn = c
if mn == 10**10:
    print("TLE")
else:
    print(mn)

