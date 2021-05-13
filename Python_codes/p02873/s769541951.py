from collections import deque
S=input()
N=len(S)+1
X=[-1 for i in range(N)]
'''
 < > >
0 2 1 0
'''
q=deque([])
for i in range(N-2):
    if S[i]==">" and S[i+1]=="<":
        X[i+1]=0
        q.append(i+1)
if S[0]=="<":
    q.append(0)
    X[0]=0
if S[N-2]==">":
    q.append(N-1)
    X[N-1]=0

while(len(q)>0):
    r=q.popleft()
    for p in [r-1,r+1]:
        if not(0<=p<N):
            continue
        if (p<r and S[p]==">") or (p>r and S[r]=="<"):
            if X[p]<=X[r]:
                X[p]=X[r]+1
                q.append(p)
#print(X)
print(sum(X))
