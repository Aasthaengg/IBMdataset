S = input()
w = int(input())

sl = []
ans = ''
tmp_s = ''
for i, s in enumerate(S):
    tmp_s += s
    if (i+1) % w == 0:
        ans += tmp_s[0]
        tmp_s = ''
else:
    if len(tmp_s) >= 1:
        ans += tmp_s[0]
print(ans)
