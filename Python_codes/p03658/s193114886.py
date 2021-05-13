N,K=map(int,input().split())
l=list(map(int,input().split()))
l=sorted(l)
total=0
t_ans=0
for i in range(N):
    total+=l[i]
for i in  range(N-K):
    t_ans+=l[i]
print(total-t_ans)