n = int(input())
b = list(map(int, input().split()))
a = []
while n > 0:
    x = -1
    for i in range(n):
        if b[i] == i + 1:
            x = i
    if not x == -1:
        b.pop(x)
        a.append(x + 1)
    else:
        print(-1)
        exit()
    n -= 1
a.reverse()
for i in a:
    print(i)