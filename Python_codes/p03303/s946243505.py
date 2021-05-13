a = list(input())
b = int(input())
if len(a)%b == 0:
  for i in range(len(a)//b):
    print(a[i*(b)],end="")
else:
  for i in range(len(a)//b+1):
    print(a[i*(b)],end="")
