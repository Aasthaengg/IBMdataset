#!python3

def LI():
    return list(map(int, input().split()))

# input
N = int(input())
AB = [LI() for _ in range(N)]

MOD = 10 ** 9 + 7


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def create_pairs():
    z = 0
    d = {}
    for a, b in AB:
        # irre
        if a == 0 and b == 0:
            z += 1
            continue
        if a == 0:
            b = 1
        elif b == 0:
            a = 1
        else:
            m = abs(gcd(a, b))
            a, b = a // m, b // m
        
        # 180
        if b < 0:
            a, b = -a, -b

        if a > 0:
            t = (a, b)
            i = 0
        else:
            t = (b, -a)
            i = 1
        if t in d:
            d[t][i] += 1
        else:
            d[t] = [0, 0]
            d[t][i] += 1
    
    return d, z


def main():
    p2 = [None] * (N + 1)
    p2[0] = 1
    for i in range(1, N + 1):
        p2[i] = p2[i - 1] * 2 % MOD
    
    d, z = create_pairs()
    ans = 1
    for x, y in d.values():
        v = p2[x] + p2[y] - 1
        ans = ans * v % MOD

    ans += z - 1
    ans %= MOD
    print(ans)
    

if __name__ == "__main__":
    main()
