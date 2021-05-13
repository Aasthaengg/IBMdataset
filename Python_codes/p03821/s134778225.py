def main():
    n = int(input())
    A, B = [], []
    for _ in range(n):
        a, b = list(map(int, input().split()))
        A.append(a)
        B.append(b)
    ans = 0
    for a, b in zip(A[::-1], B[::-1]):
        aa = a + ans
        r = aa % b
        if r != 0:
            ans += b - r
    print(ans)

if __name__ == '__main__':
    main()
