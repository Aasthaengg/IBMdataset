n = int(input())
a = list(map(int, input().split()))
i = 1; x = 0
while i < n:
    if a[i] == a[i-1]: x += 1; i += 1
    i += 1
print(x)