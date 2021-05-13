N = int(input())
s = [input() for _ in range(N)]
M = int(input())
t = [input() for _ in range(M)]
ans = 0
ex_list = []
for i in range(N):
    if s[i] not in ex_list:
        if s.count(s[i]) > t.count(s[i]):
            ans = max(s.count(s[i])-t.count(s[i]),ans)
            ex_list.append(s[i])
print(ans)