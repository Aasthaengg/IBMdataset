n = int(input())
a = list(map(int, input().split(" ")))

i = 0
c = 0
while i < n:
    if i == n - 1:
        c += 1
        break
    if a[i] == a[i+1]:
        i += 1
    elif a[i] < a[i+1]:
        while i < n - 1 and a[i] <= a[i+1]:
            i += 1
        c += 1
        i += 1
    elif a[i] > a[i+1]:
        while i < n - 1 and a[i] >= a[i+1]:
            i += 1
        c += 1
        i += 1
print(c)