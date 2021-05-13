import math
def main5():
    N, M = map(int, input().split())
    S = input()
    T = input()

    G = math.gcd(N, M)
    L = (N * M) // G

    for i in range(G):
        if S[i * N // G] != T[i * M // G]:
            print(-1)
            exit()

    print(L)

if __name__ == "__main__":
    main5()