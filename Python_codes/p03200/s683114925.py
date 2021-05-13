S = list(str(input()))
k = 0
t = -1
N = len(S)
for i in range(N):
  if S[i] == 'B':
    k += N - i - 1
    t += 1
ans = k -  t*(t+1)/2
print(int(ans))