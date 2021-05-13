s = input()
w = int(input())
a = ""
b = 0
c = 0
if len(s) % w == 0:
  c = len(s)//w
else:
  c = (len(s)//w)+1
for i in range(c):
  a = a + s[b]
  b = b + w
print(a)