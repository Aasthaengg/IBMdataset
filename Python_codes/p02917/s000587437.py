n = int(input())
b = list(map(int, input().split()))

s = b[0]
for i in range(1, n - 1):
    if b[i] >= b[i - 1]:
        s += b[i - 1]
    else:
        s += b[i]
s += b[n - 2]
print(s)