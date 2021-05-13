S = input()
cntC = 0
cnt_ = 0
ans = "WA"
N = len(S)
if S[0] == 'A':
  for i in range(2, N-1):
    if S[i] == 'C':
      cntC += 1
    elif S[i].islower():
      cnt_ += 1
  if cntC == 1 and cnt_ == N-4:
    if S[1].islower() and S[N-1].islower():
      ans = "AC"
print(ans)