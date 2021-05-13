S = input()
l = len(S)
mod = int(1e9) + 7

'''def saiki(s):
  if s == "0":
    return 1
  elif s == "1":
    return 3
  else:
    if s[0] == '0':
      return saiki(s[1:])
    else:
      SS = 2*saiki(s[1:]) + 3 ** (len(s) - 1)
      return SS'''

cnt = int(S[l-1]) * 2 + 1
base = 3
for i in range(l-1, 0, -1):
  x = int(S[i-1])
  cnt *= x+1
  cnt += base * int(x)
  cnt %= mod
  base *= 3
  base %= mod
print(cnt)