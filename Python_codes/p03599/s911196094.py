from itertools import product

A,B,C,D,E,F = map(int, input().split())
num_a = F // (100 * A)
num_b = F // (100 * B) 
num_c = int((F * E / (E + 100)) // C)
num_d = int((F * E / (E + 100)) // D)

def check_w(w_mizu, w_sato, F):
  return w_mizu + w_sato <= F

def check_tokeru(w_mizu, w_sato, E):
  return 100 * w_sato / (w_mizu + w_sato) <= 100 * E / (100 + E)

def culc_density(w_mizu, w_sato):
  return 100 * w_sato / (w_mizu + w_sato)

max = [100 * A, 0, 0]  # total, sato, density
for _a, _b,  in product(range(num_a + 1), range(num_b + 1)): 
  w_mizu = (A * _a + B * _b) * 100
  if w_mizu == 0 or w_mizu >= F:
    continue
    
  for _c, _d in product(range(num_c + 1), range(num_d + 1)):
    w_sato = (C * _c + D * _d)
    if w_sato == 0 or w_sato >= F or (w_mizu + w_sato) > F:
      continue
    
    density = culc_density(w_mizu, w_sato)
  
    if check_w(w_mizu, w_sato, F) and check_tokeru(w_mizu, w_sato, E):
      if max[2] < density:
        max[0] = w_mizu + w_sato
        max[1] = w_sato
        max[2] = density

if max[0]:
  print(max[0], max[1])

