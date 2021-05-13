def resolve():
    N, A, B = list(map(int, input().split()))
    base = (N // (A+B)) * A
    rem = N - (N//(A+B))*(A+B)
    ans = base
    ans += A if rem >= A else rem
    print(ans)


if '__main__' == __name__:
    resolve()