X = int(input())

k = 1
while not (k*X)%360 == 0:
    k += 1
print(k)
