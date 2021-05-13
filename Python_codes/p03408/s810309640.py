n = int(input())
s = [input() for _ in range(n)]
m = int(input())
t = [input() for _ in range(m)]

print(max(0, *[s.count(sn) - t.count(sn) for sn in set(s)]))