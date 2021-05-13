S = input()
N = len(S)

sum_s = 0
for s in S:
  sum_s += int(s)

print(max(sum_s, (N-1)*9 + int(S[0])-1))