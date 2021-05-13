S = input()

cnt = 0
ans = 0
n = 0
len_S = len(S)

while n < len_S:
  if S[n]== "A":
    cnt += 1
  elif S[n] == "B":
    if n < len_S-1:
      if S[n+1] == "C":
        ans += cnt
        n += 1
      else:
        cnt = 0
  else:
    cnt = 0
  n += 1
print(ans)