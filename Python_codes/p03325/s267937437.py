import math
n = int(input())
la = [int(w) for w in input().split()]

mrb = [math.log2(b & -b) for b in la]
print(int(sum(mrb)))
