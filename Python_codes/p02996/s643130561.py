n=int(input())
l=[]
dead=0
time=0
for i in range(n):
    a,b=map(int,input().split())
    l.append([b,a])
l.sort()
f=True
for i in l:
    dead=i[0]
    time+=i[1]
    if time>dead:
        print('No')
        f=False
        break
if f:
    print('Yes')
