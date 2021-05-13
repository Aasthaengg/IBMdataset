n = int(input())
a = list(map(int, input().split()))
s = sum(a) / n
mn = 10000
for i, j in enumerate(a):
    if mn > abs(s - j):
        mn = abs(s - j)
        ans = i
print(ans)