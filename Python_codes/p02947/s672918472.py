n = int(input())
s_cnt = {}

for _ in range(n):
    s = input()
    s = ''.join(sorted(s))
    s_cnt.setdefault(s,0)
    s_cnt[s] += 1

ans = 0
for s,cnt in s_cnt.items():
    ans += cnt*(cnt-1)//2

print(ans)