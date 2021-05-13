N = int(input())
S = []
for _ in range(N):
  S.append(input())
li = ["AC", "WA", "TLE", "RE"]
for s in li:
  print("{0} x {1}".format(s, S.count(s)))