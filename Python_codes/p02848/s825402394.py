N, S = [input() for _ in range(2)]
X = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
Y = ""
for s in S:
  Y += X[(X.index(s)+int(N))%26]
print(Y)