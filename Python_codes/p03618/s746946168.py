from collections import Counter

def main():
    A = input()
    N = len(A)
    ans = N * (N-1) // 2 + 1
    cnt = Counter(A)
    for c in cnt:
        ans -= cnt[c] * (cnt[c] - 1) // 2
    print(ans)


if __name__ == "__main__":
    main()
