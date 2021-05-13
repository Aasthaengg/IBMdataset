import sys
def input():
    return sys.stdin.readline()[:-1]
N,K=map(int,input().split())
s=[tuple(map(int,input().split())) for i in range(N)]
lx,ly=[],[]
for i in s:
    lx.append(i[0])
    ly.append(i[1])
lx.sort()
ly.sort()
a=10**20
t=N-K
for i in range(N-1):
    for j in range(i+1,N):
        for k in range(N-1):
            for m in range(k+1,N):
                S=(lx[j]-lx[i])*(ly[m]-ly[k])
                if S>=a:
                    continue
                c=0
                for n in s:
                    if lx[i]<=n[0]<=lx[j] and ly[k]<=n[1]<=ly[m]:
                        continue
                    c+=1
                    if c>t:
                        break
                else:
                    a=S
print(a)