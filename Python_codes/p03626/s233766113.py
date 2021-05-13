N = int(input())
S1 = input()
S2 = input()
r = 1
s = 0
for i in range(N):
  p = s
  if s == 0:
    if S1[i] == S2[i]:
      r = r*3%1000000007
      s = 1
    else:
      r = r*6%1000000007
      s = 2
  elif s == 1:
    if S1[i] == S2[i]:
      r = r*2%1000000007
      s = 1
    else:
      r = r*2%1000000007
      s = 2
  elif s == 2:
    s = 3
  elif s == 3:
    if S1[i] == S2[i]:
      r = r*1%1000000007
      s = 1
    else:
      r = r*3%1000000007
      s = 2
  #print(S1[i], S2[i], p, s, r)
print(r)
