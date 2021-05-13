dic = {}
dic1 = {}
s=input()
t=input()
ans = "Yes"
for i in range(len(s)):
  try:
    if dic[s[i]]!=t[i]:
      ans = "No"
  except:
    dic[s[i]] = t[i]
  try:
    if dic1[t[i]]!=s[i]:
      ans = "No"
  except:
    dic1[t[i]] = s[i]
print(ans)