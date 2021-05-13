s = input()
ans = 1000
for i in range(len(s)-2):
  num = abs(753-(int(s[i]+s[i+1]+s[i+2])))
  ans = min(ans,num)
print(ans)