from collections import Counter
def main():
    n = int(input())
    A = list(map(int, input().split()))
    L = Counter([i + a for i, a in enumerate(A)])
    R = Counter([i - a for i, a in enumerate(A)])
    ans = 0
    for key in R.keys():
        ans += L[key] * R[key]
    print(ans)

if __name__ == '__main__':
    main()
