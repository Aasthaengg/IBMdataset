def prime(x):
    if  x == 2:
        return True
    elif x < 2 or  x %2 == 0:
        return False
    i = 3
    while i <= x**(1/2):
        if x % i == 0:
            return False
        i = i + 2

    return True

L = []
while True:
    try:
        i = int(input())
        L.append(i)
    except EOFError:
        break
K = 0
for i in range(len(L)):
    if prime(L[i]):
        K += 1

print(K)
