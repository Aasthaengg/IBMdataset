import math
a = [int(input()) for i in range(5)]
w = [ (10 - i % 10) % 10 for i in a]
print(sum(a)+sum(w)-max(w))
