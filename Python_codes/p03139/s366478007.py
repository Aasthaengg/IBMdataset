N, A, B = map(int, input().split())
print("%d %d" % (min(A, B), max((A+B)-N, 0)))