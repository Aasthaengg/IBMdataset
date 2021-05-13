n,x = map(int,input().split())
a = list(map(int,input().split()))
a.sort()
for i in range(n):
    x = x-a[i]
    if x < 0:
        print(i)
        break
    if i == n-1:
        if x == 0:
            print(n)
        else:
            print(n-1)
