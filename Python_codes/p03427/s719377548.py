N = list(map(int, list(input())))
# print(N)
intN = int("".join(list(map(str, N))))
sumN = sum(N)

for x in range(len(N)):
    if x == 0:
        N[x] = N[x] - 1
    else:
        N[x] = 9
intN2 = int("".join(list(map(str, N))))
sumN2 = sum(N)
print(max(sumN, sumN2))
