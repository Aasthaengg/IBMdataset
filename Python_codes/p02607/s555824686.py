n = int(input())
a = list(map(int, input().split()))

for i in range(len(a)):
    if i % 2:
        a[i] = 0
    else:
        a[i] = a[i] % 2
print(sum(a))
