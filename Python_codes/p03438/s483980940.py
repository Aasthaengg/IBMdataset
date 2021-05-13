n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

j = sum(b) - sum(a)
c = [0, 0]
for i in range(n):
    if a[i] > b[i]:
        c[0] += a[i] - b[i]
    if a[i] < b[i]:
        c[1] += -(-(b[i]-a[i])//2)

print("Yes" if max(c) <= j else "No")
