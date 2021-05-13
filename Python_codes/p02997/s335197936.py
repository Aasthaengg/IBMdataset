from itertools import combinations 
n,k=map(int,input().split())
m = (n-1)*(n-2)//2
if k>m:
    print(-1)
else:
    es = []
    for i in range(2,n+1):
        es.append('1 %d' % i)
        
    idx = 0
    for i,j in combinations(range(2,n+1),2):
        if idx == m-k:
            break
        es.append('%d %d' % (i,j))
        idx +=1
    print(len(es))
    print(*es,sep="\n")