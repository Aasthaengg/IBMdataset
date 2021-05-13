n = int(input())
s = [input() for i in range(n)]
m = int(input())
t = [input() for i in range(m)]

maxCount = 0
for i in s:
    if s.count(i) - t.count(i) > maxCount:
        maxCount = s.count(i) - t.count(i)
print(maxCount)