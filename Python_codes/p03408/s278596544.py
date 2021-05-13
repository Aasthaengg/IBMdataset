N = int(input())
s = [input() for i in range(N)]
M = int(input())
t = [input() for i in range(M)]

ans = 0
for i in s:
    if s.count(i) - t.count(i) > ans:
        ans = s.count(i) - t.count(i)
print(ans)
