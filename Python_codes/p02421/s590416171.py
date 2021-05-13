n = int(input())

t_score = 0
h_score = 0


for i in range(n):
 t, h = input().split()
 if t == h:
  t_score += 1
  h_score += 1
  continue
 if len(t) >= len(h):
  for j in range(len(h)):
   if ord(t[j]) > ord(h[j]):
    t_score += 3
    break
   elif ord(t[j]) < ord(h[j]):
    h_score += 3
    break
  else:
   t_score += 3
 elif len(t) < len(h):
   for j in range(len(t)):
    if ord(t[j]) > ord(h[j]):
     t_score += 3
     break
    elif ord(t[j]) < ord(h[j]):
     h_score += 3
     break
   else:
    h_score += 3

   
print("{0} {1}".format(t_score, h_score))