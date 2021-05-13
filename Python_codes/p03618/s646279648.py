A = input()

pre_ch = {}
pre_ch_cnt = []
for i, c in enumerate(A):
  if c in pre_ch:
    pre_ch_cnt.append(pre_ch_cnt[pre_ch[c]] + 1)
  else:
    pre_ch_cnt.append(0)
  pre_ch[c] = i

s_cnt = [1]
for i, c in enumerate(A):
  s_cnt.append(s_cnt[i])
  s_cnt[i + 1] += i - pre_ch_cnt[i]

print(s_cnt[len(A)])