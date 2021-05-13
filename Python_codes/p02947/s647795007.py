N = int(input())
S = [input() for _ in range(N)]

for i in range(N):
  S[i] = ''.join(sorted(S[i]))

S_lst = {}
for i in range(N):
  if S[i] in S_lst:
    S_lst[S[i]] += 1
  else:
    S_lst[S[i]] = 1

#nC2 の計算
sum_ = 0
for key in S_lst:
    sum_ += int((S_lst[key] * (S_lst[key] - 1)) / 2)

print(sum_)