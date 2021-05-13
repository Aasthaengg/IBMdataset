X = int(input())
s = [0] * (X + 1)
for i in range(1, 1001):
    for j in range(2, 1001):
        n = i**j
        if n > X: break
        s[n] += 1
for i in range(X, 0, -1):
    if s[i]:
        print(i)
        exit()
