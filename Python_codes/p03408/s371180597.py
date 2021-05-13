N = int(input())
s = [input() for _ in range(N)]
M = int(input())
t = [input() for _ in range(M)]
print(max(max([s.count(e)-t.count(e) for e in s+t]),0))
