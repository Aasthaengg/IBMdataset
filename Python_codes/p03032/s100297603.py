import sys
input = sys.stdin.readline
N,K = map(int,input().split())
V = list(map(int,input().split()))

D = []
ans = []

for i in range(K+1):
    for j in range(K-i+1):
        if i + j > N:
            break
        D.append(V[:i]+V[N-j:])

for d in D:
    for x in range(K-len(d)):
        if d==[]:
            break
        elif min(d)<0:
            d.pop(d.index(min(d)))

        elif min(d)>0:
            break
        
    if d==[]:
        ans.append(0)
    elif sum(d)>0:
        ans.append(sum(d))

if max(ans)>0:
    print(max(ans))

else:
    print(0)