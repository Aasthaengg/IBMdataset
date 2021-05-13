# B Battle

A, B, C, D = map(int, input().split())

t_kill_a = C // B
a_kill_t = A // D

if C % B != 0:
  t_kill_a += 1
if A % D != 0:
  a_kill_t += 1

if t_kill_a <= a_kill_t:
  print("Yes")
else:
  print("No")