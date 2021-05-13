s = input()
t = input()
S = sorted(s)
T = sorted(t)[::-1]
if S < T:  print("Yes")
else:  print("No")