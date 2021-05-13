n = input()
s = len(n)
s1 = n[:s//2]
s2 = n[-1 * (s//2):]
s2 = s2[::-1]
ans = 0
for i in range(s//2):
  if s1[i] != s2[i]:
    ans += 1
print(ans)    

