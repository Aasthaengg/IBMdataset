import sys
def input(): return sys.stdin.readline().rstrip()

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))

    K -= 1
    a1_i = A.index(1)
    left = (a1_i + K - 1) // K
    right = (N - 1 - (left * K) + K - 1) // K
    print(left + right)

if __name__ == '__main__':
    main()
