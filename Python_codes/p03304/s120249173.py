def main():
    n, m, d = (int(i) for i in input().split())
    if d == 0:
        ans = 1/n
        ans *= (m-1)
        print(ans)
    else:
        ans = 2*(n-d)/n**2
        ans *= (m-1)
        print(ans)


if __name__ == '__main__':
    main()
