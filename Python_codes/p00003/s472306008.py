num = int(input())
for i in range (num):
    a=sorted(list(map(int,input().split())))
    if a[0]**2+a[1]**2 == (a[2])**2:
        print("YES")
    else:
        print("NO")