N=int(input())
p=[]
for i in range(N):
    p.append(int(input()))
a=0
for i in range(N):
    if p[i]==max(p):
        a+=p[i]//2
        p.remove(p[i])
        break
for i in range(N-1):
    a+=p[i]
print(a)