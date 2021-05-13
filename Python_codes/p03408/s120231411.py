import statistics
n = int(input())
s = [input() for i in range(n)]
m = int(input())
t = [input() for i in range(m)]
ans = 0
for i in s:
    tmp = s.count(i) - t.count(i)
    if ans <= tmp:
        ans = tmp
print(ans)