import sys

input = sys.stdin.readline

def main():
    ans = ''
    n = '\n'
    A, B, K = map(int, input().split())
    AK = min(A+K, B)
    for i in range(A, AK):
        ans += str(i) + n
    BK = max(B-K+1, AK)
    for i in range(BK, B+1):
        ans += str(i) + n
    print(ans)

if __name__ == '__main__':
    main()