s0 = input()
t0 = input()
list_s0 = list(s0)
list_t0 = list(t0)
list_s0.sort()
list_t0.sort(reverse = True)
s1 = "".join(list_s0)
t1 = "".join(list_t0)
if s1 < t1:
  print("Yes")
else:
  print("No")