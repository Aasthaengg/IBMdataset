n = int(input())
a = [int(input()) for _i in range(n)] + [-1]

result = -1
for i in range(n):
    if a[i-1] == a[i]:
        result += a[i]
    elif a[i-1] + 1 == a[i]:
        result += 1
    elif a[i-1] > a[i]:
        result += a[i]
    else:
        result = -1
        break
print(result)