S = input()
dic = {}

for s in S:
  dic[ord(s)] = True
  
for i in range(97, 97+26):
  if i not in dic:
    print(chr(i))
    exit()

print('None')