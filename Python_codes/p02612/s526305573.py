N = int(input().rstrip())
m = N % 1000
r = m
if m != 0: 
    r = 1000 - m

print(r)
