s = list(input())
k = int(input())
for i in range(len(s)):
  dp = 26-ord(s[i])+97
  if k >= dp and s[i] != "a":
    k-=dp
    s[i] = "a"
    if k == 0:
      break
else:
  s[-1] = chr((ord(s[-1])-97+k)%26+97)
print(*s,sep="")