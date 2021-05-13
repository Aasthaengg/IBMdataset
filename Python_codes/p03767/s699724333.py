n = int(input())
a = list(map(int, input().split()))

a.sort(reverse=True)

s = 0
for x in range(1, 2*n+1, 2):
    s += a[x]

print(s)
