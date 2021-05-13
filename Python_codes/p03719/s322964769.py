def func(a, b, c):
  if (a <= c <= b):
    print("Yes")
  else:
    print("No")
  
s = input().split()
func(int(s[0]), int(s[1]), int(s[2]))