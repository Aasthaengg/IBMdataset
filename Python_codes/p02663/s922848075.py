def main():
    H1, M1, H2, M2, K = (int(i) for i in input().split())
    h = H2 - H1
    m = M2 - M1
    ans = h*60 + m - K
    if ans > 0:
        print(ans)
    else:
        print(0)


if __name__ == '__main__':
    main()
