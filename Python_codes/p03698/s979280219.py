s = input()
s_list = []
for i in range(len(s)):
  if s[i] in s_list:
    print("no")
    exit()
  s_list.append(s[i])
print("yes")