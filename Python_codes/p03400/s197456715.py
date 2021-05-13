n = int(raw_input())
d,x = map(int, raw_input().split())
def f(ai,d): return 1 + (d-1)/(ai)
print x + sum([f(int(raw_input()),d)  for _ in range(n)] or [0])