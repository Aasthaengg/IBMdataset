s = list(input())

ans = []
for i in range(0,len(s)-2):
  d = int("".join(s[i]+s[i+1]+s[i+2]))
  ans.append(abs(d-753))
  
print(min(ans))
