N = int(input())
S = input()
maxi = 0
for i in range(1,N):
  a = S[0:i]
  b = S[i:]
  aa = set(a)
  bb = set(b)
  ans = bb&aa
  if len(ans) > maxi:
    maxi = len(ans)
print(maxi)