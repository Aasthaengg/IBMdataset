s = input()
n = len(s)
a, b = 0, 0
for i in s:
  if i == '1':
    a+=1
b = n-a

print(min(a,b)*2)