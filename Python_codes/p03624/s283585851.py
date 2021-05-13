ans = []
s = input()
for i in range(26):ans.append(0)
for i in s:
  ans[ord(i)-97] = 1
for i in range(26):
  if(ans[i]==0):print(chr(97+i));exit()
print("None")