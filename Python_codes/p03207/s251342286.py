N=int(input())
l=[]
for i in range(N):
    p=int(input())
    l.append(p)
p=sorted(l)
print(sum(p[0:N-1])+int(p[N-1]/2))