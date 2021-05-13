n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

pos = 0
neg = 0

for i in range(n):
    dif = b[i]-a[i]

    if dif > 0:
        pos += dif//2
    elif dif < 0:
        neg += dif

neg = abs(neg)

print("Yes" if pos >= neg else "No")