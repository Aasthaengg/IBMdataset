from collections import defaultdict
s = input()
t = input()
cnt_s = defaultdict(int)
cnt_t = defaultdict(int)
for i in range(len(s)):
    cnt_s[s[i]] += 1
    cnt_t[t[i]] += 1

cnt_s = sorted(cnt_s.values())
cnt_t = sorted(cnt_t.values())
if len(cnt_s) != len(cnt_t):
    ans = "No"
else:
    ans = "Yes"
    for i in range(len(cnt_s)):
        if cnt_s[i] != cnt_t[i]:
            ans = "No"
            break
print(ans)