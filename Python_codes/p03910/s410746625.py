n = int(input())
k = int((2*n)**.5)
for i in range(k, k*(k+1)+1):
    if 2*n >= i*(i+1):
        continue
    k = i
    break


def sigma(a, b):
    if a == b:
        return a
    elif b < a:
        return 0
    else:
        return (a+b)*(b-a+1)//2

excess = sigma(1, k)-n
for i in range(1, k+1):
    if i == excess:
        continue
    print(i)
