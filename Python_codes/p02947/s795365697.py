n = int(input())
s_cnt = {}

ans = 0
for _ in range(n):
    s = input()
    s = ''.join(sorted(s))
    s_cnt.setdefault(s,0)
    ans += s_cnt[s]
    s_cnt[s] += 1

print(ans)