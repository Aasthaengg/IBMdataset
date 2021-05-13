n=int(input())
for j in range(n):
    l =input().split()
    a=[int(l[i]) for i in range(3)]
    a=sorted(a)
    if a[0]**2+a[1]**2==a[2]**2:
        print("YES")
    else:
        print("NO")