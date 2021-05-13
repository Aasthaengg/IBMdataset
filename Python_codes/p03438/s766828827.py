n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

count = 0
for i in range(n):
    if a[i] < b[i]:
        count += (b[i] - a[i]) // 2
    else:
        count += b[i] - a[i]

print("Yes" if count >= 0 else "No")