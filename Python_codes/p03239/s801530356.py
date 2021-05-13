N,T = list(map(int,input().split()))
CT = []
for i in range(N):
    CT.append(list(map(int,input().split())))
out = 10**5
ind = N
for i in range(N):
    if CT[i][1]<=T and CT[i][0]<out:
        out = CT[i][0]
        ind = i
if ind==N:
    print("TLE")
else:
    print(out)
