n = int(input())
s = input()

x = 0
l =[0]
for i in range(n):
  if s[i]=='I':
    x += 1
  else:
    x -= 1
  l.append(x)
print(max(l))