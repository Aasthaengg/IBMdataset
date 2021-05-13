n, y = map(int,input().split())
y = y / 1000
f = 0
for i in range(n+1):
    for j in range(n-i+1):
        #print(i)
        if 10 * i + 5 * j + 1 * (n - i - j) == y:
            print(i)
            print(j)
            print(n - i - j)
            f = 1
            break
    if f == 1:
        break
if f != 1:
    print(-1)
    print(-1)
    print(-1)