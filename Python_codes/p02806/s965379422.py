n=input()
l=[]
m=[]
for i in range(n):
    x=raw_input().split()
    l.append(x[0])
    m.append(int(x[1]))
u=raw_input()
for i in range(n):
    if l[i]==u:
        print sum(m[i+1:])
        break