a,b = map(int,input().split())
str_A = ""
str_B = ""
for i in range(b):
  str_A += str(a)

for i in range(a):
  str_B += str(b)

if(str_A < str_B):
  print(str_A)
else:
  print(str_B)