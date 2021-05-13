import sys

input = sys.stdin.readline


def main():
    N = int(input())
    A, B = map(int, input().split())
    P = list(map(int, input().split()))

    C = [0] * 3
    for p in P:
        if p <= A:
            C[0] += 1
        elif p <= B:
            C[1] += 1
        else:
            C[2] += 1
    
    ans = min(C)
    print(ans)


if __name__ == "__main__":
    main()
