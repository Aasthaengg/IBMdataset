S = input()
w = int(input())
l = len(S)
ret = ""
if l % w:
  for i in range(1 + l // w):
    ret += S[i * w]
else:
  for i in range(l // w):
    ret += S[i * w]
print(ret)