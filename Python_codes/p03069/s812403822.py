N,S = open(0).read().split()
N=int(N)
S=[s == "." for s in list(S)]

w = sum([1 if s else 0 for s in S])
b = 0
m = w + b
for s in S:
    if s:
        w -= 1
    else:
        b += 1
    m = min(m, w + b)
print(m)
