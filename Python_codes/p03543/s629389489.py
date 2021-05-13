s = input()
l = [int(s[i]) for i in range(4)]
a, b, c, d = map(int, l)
m = 100*a+10*b+c
n = 100*b+10*c+d
if m%111 == 0 or n%111 == 0:
  print("Yes")
else:
  print("No")