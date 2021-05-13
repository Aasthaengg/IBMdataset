n, t = map(int,input().split())
a = list(map(int, input().split()))

result = {}
m = 0
checker = []
for i in range(1, n):
    if m<a[-i]:
        m = a[-i]
    checker.append(m)
checker = checker[::-1]
for i in range(n-1):
    s = checker[i]-a[i]
    if s in result:
        result[s] += 1
    else:
        result[s] = 1
x = max(result.items())
print(x[1])