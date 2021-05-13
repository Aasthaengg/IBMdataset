s=input()
cnt=0
for i in range(len(s)):
  if s[i] == 'o':
    cnt+=1
print("YES" if cnt >= 8-(15-len(s)) else "NO")
