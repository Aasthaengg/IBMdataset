n = int(input())
a = list(map(int, input().split()))
a.sort()

i = 0
while i < n-1:
    x = a[i+1] % a[i]
    a[i+1] = a[i]
    a[i] = x
    if a[i] == 0:
        i += 1
print(a[i])
