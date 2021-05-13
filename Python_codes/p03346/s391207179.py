import sys
input=sys.stdin.readline

def main():
    N = int(input())
    P = []
    for _ in range(N):
        P.append(int(input()))

    # Q[i]: P[i] から左を見たとき、1ずつ増加して昇順にある要素の数
    Q = [0]*(N+1)
    for p in P:
        Q[p] = Q[p-1] + 1 # p-1 だけを見ればよい

    print(N-max(Q))

if __name__ == '__main__':
    main()
