L = input().split()
a,b = map(int, input().split())
if input()==L[0]:
  a -= 1
else:
  b -= 1
print(str(a) + ' ' + str(b))