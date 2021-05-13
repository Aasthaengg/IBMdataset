n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

ca = cb = 0
for i in range(n):
    if a[i] > b[i]:
        ca += a[i] - b[i]
    elif a[i] < b[i]:
        cb += (b[i] - a[i])//2
if cb >= ca:
    print("Yes")
else:
    print("No")
