def resolve():
    n = int(input())
    S = list(map(int, input().split()))
    if n % 2 == 0:
        sum_a = (1 + max(S)) * (n // 2)
    else:
        sum_a = (2 + max(S)) * (n // 2)
    if sum(S) == sum_a:
        ans = pow(2, n // 2, (10 ** 9 + 7))
    else:
        ans = 0

    print(ans)

if __name__ == '__main__':
    resolve()
