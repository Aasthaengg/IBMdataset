s = input()
K = int(input())

rlt = ''

for i in range(len(s)-1):
  c = (26-ord(s[i])+ord('a'))%26
  if K >= c:
    rlt += 'a'
    K -= c
  else:
    rlt += s[i]
    
rlt += chr((K + ord(s[-1]) - ord('a'))%26 + ord('a'))
print(rlt)