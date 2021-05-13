n,k,q=map(int,input().split())
a,b=[int(input()) for _ in range(q)],[0]*n
for i in a:
    b[i-1]+=1
for i in b:
    print('Yes' if i+k-q>0 else 'No')