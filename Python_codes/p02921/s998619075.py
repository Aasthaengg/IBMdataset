str1 = input()
str2 = input()
ans = 0
for i in range(0, 3):
  if str1[i] == str2[i]: ans += 1
    
print(ans)