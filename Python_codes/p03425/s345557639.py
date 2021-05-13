n = int(input())
s = [input() for _ in range(n)]

name_cnt = {'M': 0, 'A': 0, 'R': 0, 'C': 0, 'H': 0}
for s_i in s:
    if s_i[0] in name_cnt.keys():
        name_cnt[s_i[0]] += 1

name_set = set()
name_chars = list(name_cnt.keys())

ans = 0
for i in range(0, 5):
    for j in range(i + 1, 5):
        for k in range(j + 1, 5):
            ans += name_cnt[name_chars[i]] * name_cnt[name_chars[j]] * name_cnt[name_chars[k]]
print(ans)
