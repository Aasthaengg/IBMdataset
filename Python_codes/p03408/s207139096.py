N = int(input())
s = ["" for _ in range(N)]
for i in range(N):
    s[i] = input()
M = int(input())
t = ["" for _ in range(M)]
for i in range(M):
    t[i] = input()

s_set = list(set(s))
t_set = list(set(t))

ans = ""
INF = -float("inf")

for i in s_set:
    score = s.count(i) - t.count(i)
    if INF < score:
        INF = score
        ans = i
for i in t_set:
    score = s.count(i) - t.count(i)
    if INF < score:
        INF = score
        ans = i

if INF < 0:
    print(0)
else:
    print(INF)
