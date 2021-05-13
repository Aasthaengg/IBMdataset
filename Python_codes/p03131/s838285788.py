def main():
    K, A, B = map(int, input().split())
    ans = 0

    if A >= B:
        ans = K + 1
    else:

        if abs(A - B) <= 2:
            ans = K + 1

        else:
            if K >= A - 1 + 2:
                ans += B
                K -= (A + 1)

                if abs(A - B) <= 2:
                    r, m = divmod(K, A)
                    ans += r * B + m
                else:
                    r, m = divmod(K, 2)
                    ans += (B - A) * r + m
            else:
                ans = K + 1

    print(ans)

if __name__ == "__main__":
    main()