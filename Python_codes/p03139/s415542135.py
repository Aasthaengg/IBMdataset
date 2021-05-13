N, A, B = [int(x) for x in input().split()]
ma = min(A,B)
mi = max(0,(A+B)-N)
print("{} {}".format(ma,mi))