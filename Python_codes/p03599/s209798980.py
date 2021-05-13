a, b, c, d, e, f = map(int, input().split())

water = [False]*(f+1)
suger = [False]*(f+1)

for i in range(0, f+1, a*100):
  water[i] = True
for i in range(f+1):
  if (i == 0 or water[i]) and i+b*100 <= f:
    water[i+b*100] = True
  
for i in range(0, f+1, c):
  suger[i] = True
for i in range(f+1):
  if (i == 0 or suger[i]) and i+d <= f:
    suger[i+d] = True

ans_w, ans_s = a*100, 0
for i in range(f+1):
  if water[i] == False:
    continue
  for j in range(f, -1, -1):
    if suger[j] == False or j*(100+e) > (j+i)*e or j+i > f:
      continue
    if j*(ans_w+ans_s) > (j+i)*ans_s:
      ans_w, ans_s = i, j
    break
print(ans_w+ans_s, ans_s)