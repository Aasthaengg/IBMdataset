alpha_dict = {}
for i,c in enumerate(range(ord('A'),ord('Z')+1)):
  alpha_dict[chr(c).lower()] = 0

s = list(input())
for i in range(len(s)):
  alpha_dict[s[i]] += 1

for k, v in alpha_dict.items():
  if v == 0:
    print(k)
    exit()
print('None')