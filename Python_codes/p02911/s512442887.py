n,k,q = map(int,input().split())
tokuten = [(k-q) for i in range(n+1)]
tokuten[0]=0
for i in range(q):
    a = int(input())
    tokuten[a]+=1
for i in range(1,n+1):
    if tokuten[i]>0:
        print('Yes')
    else:
        print('No')