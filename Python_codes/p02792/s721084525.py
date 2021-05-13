import math
N = input()
d = list(map(int, list(N)))
N = int(N)

comb = [0] * 10 * 10
for i in range(1,N + 1):
  top = str(i)[0]
  bot = str(i)[-1]
  pair = 0
  pair = int(str(i)[0]) * 10 + int(str(i)[-1])
  comb[pair] += 1

ans = 0

for i, var in enumerate(comb):
  top = int(str(i)[0])
  bot = int(str(i)[-1])
  if top == bot:
    ans += var ** 2
  else:
    ans += comb[top * 10 + bot] * comb[top + bot * 10]
    

print(ans)


