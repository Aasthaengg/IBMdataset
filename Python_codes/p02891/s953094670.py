S = list(input())
N = len(S)
K = int(input())
if N == 1:
  print(K//2)
  quit()

S = S + S + S
ans_first = ans_odd = ans_even = 0
for i in range(1, N):
  pre_s = S[i-1]
  s = S[i]
  if s == pre_s:
    ans_first += 1
    S[i] = '#'

for i in range(N, 2*N):
  pre_s = S[i-1]
  s = S[i]
  if s == pre_s:
    ans_even += 1
    S[i] = '#'

for i in range(2*N, 3*N):
  pre_s = S[i-1]
  s = S[i]
  if s == pre_s:
    ans_odd += 1
    S[i] = '#'

k_even = K // 2
k_odd = K - k_even - 1
print(ans_first + k_odd*ans_odd + k_even*ans_even)