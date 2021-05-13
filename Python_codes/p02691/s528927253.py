def main():
    N = int(input())
    A = [int(i) for i in input().split()]
    B = [(i+1)+a for i, a in enumerate(A)]
    from collections import Counter
    c = Counter()

    ans = 0
    for j in range(N):
        i = j
        v = (j+1) - A[j]
        ans += c[v]
        c[B[i]] += 1

    print(ans)


if __name__ == '__main__':
    main()
