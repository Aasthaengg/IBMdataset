a,b,k=map(int,input().split())
l=[]
for i in range(k):
    if a+i<=b: l.append(a+i)
    if a<=b-i: l.append(b-i)
l=sorted(set(l))
for i in range(len(l)):
    print(l[i])