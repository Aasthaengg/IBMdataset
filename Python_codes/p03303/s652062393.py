s = input()
w = int(input())
a = ''
if len(s)%w == 0:
  b = len(s)//w
else:
  b = len(s)//w+1

for i in range(b):
  a += s[i*w]
print(a)