n=input()
l=[]
m=[]
for i in range(n):
    x=raw_input().split()
    l.append(x[0])
    m.append(int(x[1]))
u=raw_input()
print sum(m[l.index(u)+1:])