n, x = map(int, input().split())
a = list(map(int, input().split()))
a.sort()
y = x
if y < a[0]:
    print(0)
else:
    for i in range(n):
        x = x - a[i]
        if x > 0:
            continue
        elif x == 0:
            print(i+1)
            break
        elif x < 0:
            print(i)
            break
if x > 0 and y > a[0]:
    print(n-1)