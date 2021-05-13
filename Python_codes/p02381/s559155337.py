import math
S = list(map(int, open(0).read().split()))
i = 0
while i < len(S):
    n = S[i]
    if n == 0:
        break
    s = S[i+1:i+1+n]
    i+=(1+n)
    avg = sum(s) / n
    a2 = sum([(avg - x)**2 for x in s]) / n
    a = math.sqrt(a2)
    print("{:.8f}".format(a))

