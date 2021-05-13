n = int(input())
a = list(map(int, input().split(' ')))

ans = 0
i = 0
while n > i:
    ans += 1
    while n > i + 1 and a[i] == a[i+1]:
        i += 1
    if n == i + 1:
        break
    if a[i] < a[i+1]:
        while n > i + 1 and a[i] <= a[i+1]:
            i += 1
    else:
        while n > i + 1 and a[i] >= a[i+1]:
            i += 1
    i += 1
print(ans)
