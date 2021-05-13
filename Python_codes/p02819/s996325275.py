x = int(input())

eratostenes = [True] * 10**6
for i in range(2, len(eratostenes)):
    if eratostenes[i]:
        for j in range(i * 2, len(eratostenes), i):
            eratostenes[j] = False
for i in range(x, len(eratostenes)):
    if eratostenes[i]:
        print(i)
        exit()