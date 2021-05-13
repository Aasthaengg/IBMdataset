a,b,k=map(int,input().split())
L=[]
for i in range(a,a+k):
    if i<=b:
        L.append(i)
for i in range(b+1-k,b+1):
    if i>=a:
        L.append(i)
for l in sorted(set(L)):
    print(l)