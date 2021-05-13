t_health, t_strength, a_health, a_strength = (int(i) for i in input().split())

while t_health > 0 and a_health > 0:
  a_health -= t_strength
  if a_health <= 0:
    print('Yes')
    break
  t_health -= a_strength
  if t_health <= 0:
    print('No')
    break
