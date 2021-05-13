N,K =  map(int,input().split())
l = list(map(int,input().split()))
score=[]
for i in range(K,N):
    if l[i-K] < l[i]:
        print('Yes')
    else:
        print('No')
