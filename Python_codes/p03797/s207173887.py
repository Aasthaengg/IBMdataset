def resolve():
    n, m = map(int, input().split())
    ans = n
    if m < 2:
        return print(0)
    if m <= 2*n:
        return print(m//2)
    diff = m - 2*n
    ans += diff//4

    print(ans)

if __name__ == '__main__':
    resolve()