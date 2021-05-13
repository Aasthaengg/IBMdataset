X = list(map(int, [input() for _ in range(5)]))
X = sorted(X, key=lambda x: x%10)
r = 0
for x in X:
    if x % 10 == 0:
        r += x
    else:
        if r % 10 == 0:
            r += x
        else:
            r += (1+x//10) * 10
print(r)
