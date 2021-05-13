n = int(input())
a = list(map(int, input().split()))
a.sort(reverse=True)
i = 0
x = 0
y = 0
while i < n-1:
    if x == 0:
        if a[i] == a[i+1]:
            x = a[i]
            i += 1
    elif y == 0:
        if a[i] == a[i+1]:
            y = a[i]
            i += 1
    i += 1
print(x*y)