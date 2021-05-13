s=input()
count=0
l,r = 0,len(s)-1
while l<=r:
  if s[l] != s[r]: count += 1
  l += 1
  r -= 1
print(count)