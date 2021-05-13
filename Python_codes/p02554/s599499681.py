def calc(intN):  

    ret=10**intN+8**intN-2*(9**intN)
    return ret%(10**9+7)

N = int(input())

print(calc(N))