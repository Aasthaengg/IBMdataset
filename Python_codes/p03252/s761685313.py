s = input()
t = input()
S = sorted(map(s.count,set(s)))
T = sorted(map(t.count,set(t)))

if S==T:
  print("Yes")
else:
  print("No")