n,m = map(int,input().split())
lis =[0 for i in range(1,n+1)]
ac = 0
wa = 0
for i in range(m):
    p,s = input().split()
    p = int(p)
    if lis[p-1] != -1:
        if s == "AC":
            wa += lis[p-1]
            ac += 1
            lis[p-1] = -1
        else:
            lis[p-1] += 1
print(ac,wa)
