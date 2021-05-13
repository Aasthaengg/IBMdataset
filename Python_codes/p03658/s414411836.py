n,k=map(int,input().split())
l=list(map(int,input().split()))
l1 = sorted(l, reverse=True)
s=0
for i in range(k):
    s+=l1[i]
print(s)