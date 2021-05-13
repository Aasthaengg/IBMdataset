s = list(input())
t = list(input())

s_dash="".join(sorted(s))
t_dash="".join(list(reversed(sorted(t))))

if s_dash < t_dash:
  print("Yes")
else:
  print("No")
