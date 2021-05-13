a, b, x = map(int, input().split())

i = a// x
j = b// x
p = i* x
q = j* x
while i* x < a:
  i+= 1
  p = i* x
while j* x < b:
  j+= 1
  q = (j- 1)* x

ans = int((q- p)// x)+ 1

if(ans<= 0):
  print(0)
else:
  print(ans)