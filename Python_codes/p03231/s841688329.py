import fractions
def main():
    N, M = (int(_) for _ in input().split())
    S = input()
    T = input()
    g = fractions.gcd(N, M)
    for i in range(N):
        if i % (N//g) == 0 and S[i] != T[M*i//N]:
            print(-1)
            break
    else:
        print(N * M // g)
    return

if __name__ == '__main__':
    main()
