N,K = list(map(int,input().split()))
A = list(map(int,input().split()))

A_={}
for a_idx,a in enumerate(A):
    A_[a_idx+1] = a

visit={}
first={}
for n in range(N):
    visit[n+1]=0
    first[n+1]=-1
    
v=1
Loop=[]
for n in range(2*N):   
    Loop.append(v)
    if visit[v] == 0:
        first[v] = n
    visit[v]+=1
#     print(v,visit)
    if visit[v] == 2:
        break
        
    v=A_[v]

if K-first[v] < 0:
    print(Loop[K])
else:  
    ans_idx=(K-first[v])%(n-first[v])
    print(Loop[first[v]:n][ans_idx])