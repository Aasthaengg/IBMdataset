n = int(input())
s = list(input() for i in range(n))
m = int(input())
t = list(input() for i in range(m))

count = 0

for i in s:
    v = s.count(i) - t.count(i)
    if v >= count:
        count = v

print(count)