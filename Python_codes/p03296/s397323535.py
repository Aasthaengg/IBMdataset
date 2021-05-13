n = int(input())
a = list(map(int, input().split()))
cnt = 0
i = 0
while i < n - 1:
    if i < n - 2 and a[i] == a[i + 1] == a[i + 2]:
        cnt += 1
        i += 1
    elif a[i] == a[i + 1]:
        cnt += 1
    i += 1
print(cnt)