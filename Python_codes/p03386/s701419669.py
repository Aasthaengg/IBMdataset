a,b,k=map(int,input().split())
p=set()
for i in range(min(k,b-a+1)):
    p.add(a+i)
    p.add(b-i)
k=sorted(list(p))
for i in range(len(k)):
    print(k[i])