n,k,q=map(int,input().split())
d={i:0 for i in range(n)}
for i in range(q):
    a=int(input())
    d[a-1]+=1
for i in range(n):
    print("Yes" if k-q+d[i]>0 else "No")