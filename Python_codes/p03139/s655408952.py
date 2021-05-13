N, A, B = map(int, input().split())
print("{0} {1}".format(min(A, B), max(A + B - N, 0)))
