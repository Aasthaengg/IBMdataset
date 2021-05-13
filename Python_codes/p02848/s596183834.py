N=int(input())
S=input()
ans=""
for x in range(len(S)):
  t=ord(S[x])+N
  if t>90:
    t-=26
  ans+=chr(t)
print(ans)