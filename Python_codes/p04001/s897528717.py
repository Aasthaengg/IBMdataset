s = input()
import itertools
a = itertools.product([0,1],repeat=len(s)-1)

ans = 0
for x in a: # x = (0,1)
  txt = s[0]
  for i,kigo in enumerate(x):
    if kigo:
      txt += "+" + s[i+1]
    else:
      txt += s[i+1]
  ans += sum(list(map(int,txt.split('+'))))

print(ans)
