k = int(input())
L = [49]*50
t = k//50
for i in range(50):
    L[i] += t
m = k%50
for i in range(m):
    for j in range(50):
        if i == j:
            L[j] += 50
        else:
            L[j] -= 1
print(50)
print(' '.join(map(str, L)))
