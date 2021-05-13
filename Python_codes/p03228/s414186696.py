a=[]
a1,a2,c = input().split()
a.append(int(a1))
a.append(int(a2))
c = int(c)
cur = 0
for i in range(c):
    a[1-cur]+=a[cur]//2
    a[cur]//=2
    cur=1-cur
print(a[0], a[1])
