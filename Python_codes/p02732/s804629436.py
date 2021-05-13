def main():
    N = int(input())
    A = [int(i) for i in input().split()]
    from collections import Counter
    c = Counter(A)
    ans = 0
    for v in c.values():
        ans += v*(v-1)//2

    for k in range(N):
        v = c[A[k]]
        diff = -v*(v-1)//2 + (v-1)*(v-2)//2
        print(ans + (diff if v != 1 else 0))


if __name__ == '__main__':
    main()
