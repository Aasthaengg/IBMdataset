s=list(input())
t=""
for i in range(len(s)):
  if i%2==0: #0indexなので偶数に
    t+=s[i]
print(t)