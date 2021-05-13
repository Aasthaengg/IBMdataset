X = int(input())

beki = [1]
for b in range(2, int(pow(X, 0.5))+1):
    p = 2
    while pow(b, p) <= X:
        beki.append(pow(b, p))
        p += 1
print(max(beki))