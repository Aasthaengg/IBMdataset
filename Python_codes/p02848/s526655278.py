N = int(input())
S = str(input())

ans = ""

for i in range(len(S)):
  temp = ord(S[i])
  nxt = temp+N
  if nxt >= 91:
    nxt -= 26
  ans += chr(nxt)
print(ans)