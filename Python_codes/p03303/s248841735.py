s = input()
w = int(input())

i = 0
r = ""
while i < len(s):
  r += s[i]
  i += w
  
print(r)