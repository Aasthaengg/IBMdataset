n,k,q=map(int,input().split())
pts=[0]*n
for _ in range(q):pts[int(input())-1]+=1
for v in pts:print('Yes' if v+k-q>0 else 'No')