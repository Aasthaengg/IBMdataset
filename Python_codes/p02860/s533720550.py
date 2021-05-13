N = int(input())
S = input()
res = ""
s = ""
t = ""
if len(S) % 2 == 1:
  res = "No"
else:
  s = S[0:len(S)//2]
  t = S[len(S)//2: len(S)]
  if s ==t:
    res = "Yes"
  else:
    res = "No"
print(res)