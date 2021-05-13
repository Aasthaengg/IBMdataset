while input() != "0":
  l = list(map(int, input().split()))
  print("{0:.8f}".format((sum([(s - sum(l) / len(l)) ** 2 for s in l]) / len(l)) ** 0.5))
