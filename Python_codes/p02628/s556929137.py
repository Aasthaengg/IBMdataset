n,k=map(int,input().split())
p=map(int,input().split())

p=list(p)
p.sort()

a=0

for i in range(k):
    a+=p[i]

print(a)