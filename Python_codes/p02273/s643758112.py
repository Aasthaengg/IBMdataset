import cmath

def koch(n, p1, p2):
  if not n:
    return None
  s = (2*p1 + p2) / 3
  t = (p1 + 2*p2) / 3
  u = s + cmath.rect(1, cmath.pi/3) * (t - s)
  koch(n-1, p1, s)
  print(s.real, s.imag)
  koch(n-1, s, u)
  print(u.real, u.imag)
  koch(n-1, u, t)
  print(t.real, t.imag)
  koch(n-1, t, p2)

p1, p2 = 0j, 100+0j
print(p1.real, p1.imag)    
koch(int(input()), p1, p2)
print(p2.real, p2.imag)
