n,m=map(int,input().split())
s=set(i+1 for i in range(m))

for i in range(n):
    t=[int(i) for i in input().split()]
    t=set(t[1:])
    s=s&t
print(len(s))