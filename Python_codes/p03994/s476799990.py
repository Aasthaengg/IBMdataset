s = input()
k = int(input())
n = len(s)
for i in range(n):
  num = ord(s[i])
  if num == 97 or 123-num > k:
    continue
  k -= (123-num)
  s = s[:i] + 'a' + s[i+1:]
if k > 0:
  t = k%26
  s = s[:n-1] + chr(ord(s[n-1])+t)
print(s)  
