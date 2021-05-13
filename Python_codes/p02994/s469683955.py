a,b=map(int,input().split())
n=list(range(b,b+a))
o=[]
for i in n:
    o.append(abs(i))

del n[o.index(min(o))]

print(sum(n))