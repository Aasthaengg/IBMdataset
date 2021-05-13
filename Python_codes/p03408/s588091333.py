n = int(input())
s = [input() for _ in range(n)]
m = int(input())
t = [input() for _ in range(m)]

x = list(set(s))
res = 0
for str_ in x:
    res = max(res, s.count(str_) - t.count(str_))
print(res)