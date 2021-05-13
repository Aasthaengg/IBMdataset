n = int(input())
a = list(map(int, input().split()))
x = min(a)
while True:
    for i in range(n):
        if a[i] % x == 0:
            a[i] = x
        else:
            a[i] = a[i] % x
    if x == min(a):
        print(x)
        break
    else:
        x = min(a)