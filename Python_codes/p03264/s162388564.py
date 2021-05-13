def cmb(n):
    return (n * (n - 1)) / 2

k = int(input())
if (k % 2 == 0):
    print(int(cmb(k) - 2 * cmb(k / 2)))
else:   
    print(int(cmb(k) - ((cmb(k // 2) + cmb(k // 2 + 1)))))