X = input()
N = len(X)
c = 0
s, t = 0, 0
for k in range(N):
    if X[k] == "S":
        s += 1
    else:
        t += 1
        if s > 0 and t > 0:
            s -= 1
            t -= 1
            c += 2
print(N-c)
