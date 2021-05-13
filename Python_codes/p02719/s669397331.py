import sys
line = sys.stdin.readlines()[0]
n, k = [int(s) for s in line.split(" ")]
t = n // k
a1 = abs(n - (k * t))
a2 = abs(n - k * (t + 1))
answer = min(a1, a2)
print(answer)