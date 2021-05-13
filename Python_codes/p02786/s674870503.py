H=int(input())
ans=0
i=1
while H>1:
  H=H//2
  ans += i
  i *= 2
print(ans+i)