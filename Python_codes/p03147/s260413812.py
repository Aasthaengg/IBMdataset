n=0
Answer=0
N=int(input())
h=list(map(int,input().split()))
h.insert(0,0)

for i in range(N):
    if h[n]<=h[n+1]:
        m=h[n+1]-h[n]
        Answer=Answer+m
    else :
        pass
    n=n+1
print(Answer)