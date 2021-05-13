N = int(input())
a = list(map(int, input().split()))
colors = [0]*9
for ai in a:
  if ai >= 3200:
    colors[8] += 1
  else:
    colors[ai//400] = 1
    
cmin = max(1, sum(colors[0:8]))
cmax = sum(colors)

print(cmin, cmax)