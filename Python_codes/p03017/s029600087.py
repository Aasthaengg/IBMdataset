import sys
readline = sys.stdin.buffer.readline
sys.setrecursionlimit(10 ** 8)
INF = float('inf')
MOD = 10 ** 9 + 7



def main():
    int1 = lambda x: int(x) - 1
    N, A, B, C, D = map(int1, input().split())
    S = input()

    if "##" not in S[A:B + 1] and "##" not in S[C:D + 1]:
        if C > D and "..." not in S[B - 1:D + 2]:
            print("No")
        else:
            print("Yes")
    else:
        print("No")


if __name__ == '__main__':
    main()