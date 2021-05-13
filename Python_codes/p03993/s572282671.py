n = int(input())
a = list(map(int,input().split()))
c = 0

for i in range(n):
    if a[i] == -1:
        pass
    elif a[a[i] - 1] - 1 == i:
        c += 1
        a[a[i] - 1] = -1
        a[i] = -1
    else:
        pass

print(c)