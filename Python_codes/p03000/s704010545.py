n,x=map(int,input().split())
*l,=map(int,input().split())
s=[0]
for i in range(n):
    s.append(s[i]+l[i])
print(sum(t<=x for t in s))