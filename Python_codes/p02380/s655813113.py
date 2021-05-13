# AOJ ITP1_10_A

import math

def floatinput():
    a = input().split()
    for i in range(len(a)):
        a[i] = float(a[i])
    return a

def main():
    data = floatinput()
    a = data[0]; b = data[1]; C = data[2]
    S = a * b * 0.5 * math.sin(math.radians(C))
    c = math.sqrt(a ** 2 + b ** 2 - 2 * a * b * math.cos(math.radians(C)))
    L = a + b + c
    h = b * math.sin(math.radians(C))
    print(S); print(L); print(h)

if __name__ == "__main__":
    main()
