def pj(cond):
  d = {True: "Yes", False:"No"}
  print(d[cond])

K, X = [int(i) for i in input().split()]
pj(X <= K * 500)