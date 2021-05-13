import collections
n = int(raw_input())
ais = map(int,[raw_input() for _ in range(5)])
m = min(ais)
print (n + m -1) / m  + 4