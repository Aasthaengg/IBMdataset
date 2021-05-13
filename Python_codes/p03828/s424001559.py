from math import sqrt, ceil
def solve():
    n = int(input())
    keta = [0] * (n+1)
    for i in range(2, n+1):
        for j in range(2, int(pow(i, 0.5))+1):
            while i % j == 0:
                i //= j
                keta[j] += 1
        keta[i] += 1

    mod = 1000000007
    ans = 1
    keta[0] = 0
    keta[1] = 0
    for ex in keta:
        ans *= (ex + 1)
        ans %= mod
    print(ans)

if __name__ == '__main__':
    solve()