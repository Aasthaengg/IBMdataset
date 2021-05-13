n, q = list(map(int, input().split()))

s = list(input())

a = [0] * (n+1)

for i in range(1, n):
    if s[i-1] == "A" and s[i] == "C":
        a[i+1] = a[i] + 1
    else:
        a[i+1] = a[i]

for j in range(q):
    l, r = list(map(int, input().split()))
    print(a[r] - a[l])

