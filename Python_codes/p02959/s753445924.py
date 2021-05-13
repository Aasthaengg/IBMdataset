n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

s = sum(a)

for i in range(n):
    if a[i] < b[i]:
        a[i+1] = max(0, a[i+1] - (b[i] - a[i]))
        a[i] = 0
    else:
        a[i] -= b[i]


print(s-sum(a))