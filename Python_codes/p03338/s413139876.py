import collections
a=int(input())
b=input()
result=[]
for i in range(1,a):
    n=b[:i]
    m=b[i:]
    n=collections.Counter(n)
    m=collections.Counter(m)
    n,o1=zip(*n.most_common())
    m,o2=zip(*m.most_common())
    n=set(n)
    m=set(m)
    s_i=n&m
    s_i=len(s_i)
    result.append(s_i)
print(max(result))