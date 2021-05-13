from collections import Counter
N = int(input())
A = list(map(int, input().split()))

def calc():
    c = Counter(A)
    if N % 2 == 0:
        for i, v in c.items():
            if i % 2 == 0:
                return 0
            if v != 2:
                return 0
    else:
        for i, v in c.items():
            if i % 2 == 1:
                return 0
            if i == 0 and v == 1:
                continue
            if v != 2:
                return 0
    return pow(2, N//2, 10**9+7)

print(calc())        

