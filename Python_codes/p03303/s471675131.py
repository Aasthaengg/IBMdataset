s = input()
n = int(input())

ans = ""
for i in range(len(s)):
  if i % n == 0:
    ans += s[i]
    
print(ans)