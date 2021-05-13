# https://atcoder.jp/contests/agc022/submissions/9146869

s = str(input())

# 英小文字26個
alphabet = set(chr(ord('a')+i) for i in range(26))

def F_short(s):
  # 未使用の文字で最小のものを後ろに付ける
  se = alphabet - set(s)
  x = min(se)
  return s + x

def F_long(s):
  # 辞書順いちばん最後 zyx...cba
  if s == ''.join(sorted(alphabet, reverse=True)):
    return -1

  # 1文字ずつpopして、増加チャンスを待つ
  cand = []  # 末尾から除去した文字たち
  s = list(s)
  while True:
    x = s[-1]  # 末尾の文字
    if (not cand) or (x > max(cand)):
      cand.append(s.pop())
      continue
    else:
      break
  y = min(ch for ch in cand if ch > x)
  return ''.join(s[:-1]) + y

if len(s) < 26:
  ans = F_short(s)
else:
  ans = F_long(s)
print(ans)