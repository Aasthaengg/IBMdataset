n=int(input())
l=[]
for i in range(n):
    l.append(list(map(int,input().split())))
p=[a+b for a,b in l]
q=[a-b for a,b in l]
p.sort()
q.sort()
print(max(p[-1]-p[0],q[-1]-q[0]))
