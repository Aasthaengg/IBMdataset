#n=int(input())
n,k=map(int,input().split())
al=list(map(int,input().split()))
#l=[list(map(int,input().split())) for i in range(n)]

first = al[0]
for i in range(k, n):
    last = al[i]
    if first < last :
        print('Yes')
    else:
        print('No')
    first = al[i-k+1]


