X = int(input())

beki = []

for i in range(1, 33):
    for j in range(2, 11):
        beki.append(i**j)

for i in range(X):
    if X-i in beki:
        print(X-i)
        exit()
