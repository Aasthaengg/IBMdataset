MOD = 10 ** 9 + 7

def Z(): return int(input())
def ZZ(): return [int(_) for _ in input().split()]

def main():
    N, A = Z(), ZZ()
    cnt = [0] * (N)
    ng, output = 0, 1

    for a in A:
        if a == 0:
            ng += 1
            cnt[a] += 1
            continue
        cnt[a] += 1
        output *= cnt[a-1]
        output %= MOD
        cnt[a-1] -= 1
    ng = 6 if 2 <= ng <= 3 else 3 if ng == 1 else 0
    output *= ng
    output %= MOD
    print(output)

    return

if __name__ == '__main__':
    main()
