n = int(input())
s = input()
res = ""
for i in list(s):
  res += chr((ord(i) - ord('A')+n)%26+ord('A'))
  
print(res)