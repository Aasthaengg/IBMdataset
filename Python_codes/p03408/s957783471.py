N = int(input())
s = []
for i in range(N):
    s.append(input())

M = int(input())
t = []
for i in range(M):
    t.append(input())

s_set = list(set(s))
t_set = list(set(t))

ans = 0
for i in range(len(s_set)):
    y = 0
    for j in range(N):
        if s_set[i] == s[j]:
            y += 1
    for k in range(M):
        if s_set[i] == t[k]:
            y -= 1
    if y > ans:
      ans = y

print(ans)