n = int(input())
h = list(map(int, input().split()))

a = []

s = 0
for i in range(n):
    if i < n-1 and h[i] >= h[i+1]:
        s += 1
    else:
        a.append(s)
        s = 0

print(max(a))
