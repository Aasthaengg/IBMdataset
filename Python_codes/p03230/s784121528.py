n = int(input())
a = []
for i in range(1,500):
    a.append(i*(i-1)//2)
if (n in a):
    print("Yes")
    x = a.index(n)+1 #3
    ans = [[] for _ in range(x)]
    now = 1
    l = 0
    while l<x:
        for i in range(x-l-1):
            ans[l].append(now)
            ans[l+1+i].append(now)
            now += 1
        l += 1
    print(x)
    for i in range(x):
        print(x-1,*ans[i])
        
else:
    print("No")