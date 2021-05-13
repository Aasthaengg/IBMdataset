S = input()
K = int(input())
N = len(S)
A = [0]*N

ans = ""
for i in range(N):
  A[i] = (ord("z") - ord(S[i]) + 1) % 26
  if i != N-1:
    if K >= A[i]:
      K -= A[i]
      ans += "a"
    else:
      ans += S[i]
  else:
    K = K % 26
    s = ord(S[i]) + K
    if s > ord("z"):
      s -= 26
    ans += chr(s)
    
print(ans)