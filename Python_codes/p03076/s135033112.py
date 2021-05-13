ais = map(int, [raw_input() for _ in range(5)] )
ais.sort(key = lambda x:-x % 10)
s = 0
for i in range(4):
  s += (ais[i] + 9)/10 * 10
s += ais[-1]
print s