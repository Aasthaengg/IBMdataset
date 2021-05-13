S = input()
blank_cnt = len(S) - 1
ans = 0
for i in range(2 ** blank_cnt):
  formula = S[0]
  for j in range(blank_cnt):
    if (i >> j) & 1:
      formula += "+" + S[j + 1]
    else:
      formula += S[j + 1]
  ans += sum(list(map(int, formula.split("+"))))
print(ans)