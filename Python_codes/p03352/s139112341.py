s=set()
s.add(1)
x=1001
for i in range(2,1000):
    k=i*i
    while k<x:
        s.add(k)
        k*=i
#print(sorted(s))
l=[i for i in range(1001)]
for i in range(1,1001):
    if i in s:
        l[i]=i
    else:
        l[i]=l[i-1]
print(l[int(input())])