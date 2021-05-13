x = input().split()
y = input().split()
z = input()
if x[0] == z:
  y[0] = int(y[0]) - 1
elif x[1] == z:
  y[1] = int(y[1]) - 1
print(str(y[0])+' '+str(y[1]))