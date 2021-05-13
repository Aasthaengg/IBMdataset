#b

N,T = map(int,input().split())
CT=[None]*N
for i in range(N):
    CT[i] = list( map(int,input().split()) )

intime = [ct[0] for ct in CT if ct[1]<=T]
if len(intime)==0:
    print("TLE")
else:
    print(min(intime))