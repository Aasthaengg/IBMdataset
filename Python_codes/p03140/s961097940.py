import sys

read = sys.stdin.read
readline = sys.stdin.buffer.readline
sys.setrecursionlimit(10 ** 8)
INF = float('inf')
MOD = 10 ** 9 + 7


def main():
    N = int(readline())
    A = readline().decode('utf-8').strip()
    B = readline().decode('utf-8').strip()
    C = readline().decode('utf-8').strip()
    ans = 0
    for i in range(N):
        if A[i]==B[i]==C[i]:
            continue
        elif A[i]!=B[i] and B[i]!=C[i] and C[i]!=A[i]:
            ans += 2
        else:
            ans += 1
    print(ans)


if __name__ == '__main__':
    main()
