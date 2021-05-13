n = int(input())
a = list(map(int, input().split()))
a.sort()
b = [0]
for i in range(n):
    b.append(b[-1] + a[i])
count = 1
for i in range(n - 1):
    if b[n - i - 1] * 2 >= a[n - i - 1]:
        count += 1
    else:
        break
print(count)