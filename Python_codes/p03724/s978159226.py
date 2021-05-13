def Z(): return int(input())
def ZZ(): return [int(_) for _ in input().split()]

def main():
    N, M = ZZ()
    cnt = [0] * (N + 1)
    for _ in range(M):
        a, b = ZZ()
        cnt[a] += 1
        cnt[b] += 1
    print('YES' if all([c%2 == 0 for c in cnt]) else 'NO')

    return

if __name__ == '__main__':
    main()
