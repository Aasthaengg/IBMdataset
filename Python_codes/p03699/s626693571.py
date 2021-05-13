n = int(input())
a = []
for _ in range(n):
    a.append(int(input()))
total = sum(a)
if total % 10 != 0:
    print(total)
else:
    a.sort()
    index = 0
    while index < n and a[index] % 10 == 0:
        index += 1
    if index == n:
        print(0)
    else:
        print(total - a[index])