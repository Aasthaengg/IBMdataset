def Z(): return int(input())
def ZZ(): return [int(_) for _ in input().split()]

def main():
    K, T = ZZ()
    A = ZZ()
    output = 0
    for a in A: output += max(0, a - (K - a + 2) + 1)
    print(output)

    return

if __name__ == '__main__':
    main()
