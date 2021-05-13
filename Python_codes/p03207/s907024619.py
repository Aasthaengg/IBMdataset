n=int(input())
l=[]
for i in range(n):
    p=int(input())
    l.append(p)
l=sorted(l)
max_l=l[-1]
l.pop()
print(max_l//2+sum(l))