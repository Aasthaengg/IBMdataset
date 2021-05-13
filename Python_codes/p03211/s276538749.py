s = input()
n = len(s)
ans = 1000

for i in range(n-2):
  c = int(s[i])*100+int(s[i+1])*10+int(s[i+2])
  ans = min(ans,abs(753-c))
  
print(ans)