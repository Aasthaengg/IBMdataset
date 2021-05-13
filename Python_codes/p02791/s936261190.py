a = int(input())
b = list(map(int, input().split()))

m = b[0]
n = 0
for i in range(0,a):
    if m >= b[i]:
        m = b[i]
        n = n + 1
print(n)