s=input()
# アルファベット(a〜z)→数値(1〜26)小文字限定
a2n = lambda c: ord(c) - ord('a') + 1
# 数値(1〜26)→アルファベット(a〜z)
n2a = lambda c: chr(c+64).lower()

if len(s)<26:
  for i in range(1,27):
    if n2a(i) not in s:
      print(s+n2a(i))
      exit()
f=False
for i in range(1,26):
  if a2n(s[-i-1])>a2n(s[-i]):
    continue
  else:
    f=True
    break
if f==False:
  print(-1)
  exit()

ans=s[:-i-1]
mini=min([a2n(d) for d in s[-i:] if a2n(d)>a2n(s[-i-1])])
ans+=str(n2a(mini))
print(ans)
