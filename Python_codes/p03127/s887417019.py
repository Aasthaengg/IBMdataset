n = int(input())
a = list(map(int, input().split()))
a.sort()

i = 0
while True:
    x = a[i+1] % a[i]
    if x < a[i]:
        a[i+1] = a[i]
        a[i] = x
        if a[i] == 0:
            i += 1
            if i == n-1:
                break
    else:
        break
print(a[i])
