N = int(input())
A = list(map(int,input().split()))
ans = "Yes"
if N % 3 != 0:
  if len(set(A)) != 1 or list(set(A))[0] != 0:
    ans = "No"
  print(ans)
else:
  if len(set(A)) == 1:
    if list(set(A))[0] != 0:
      ans = "No"
  elif len(set(A)) == 2:
    if A.count(0) != N // 3:
      ans = "No"
  elif len(set(A)) == 3:
    A_s = list(set(A))
    for a in A_s:
      if A.count(a) != N // 3:
        ans = "No"
      elif A_s[0] ^ A_s[1] ^ A_s[2] != 0:
        ans = "No"
  else:
    ans = "No"
  print(ans)