def main():
    x = int(input())
    p, q = divmod(x, 11)
    r, s = divmod(q, 6)
    ans = 2 * p + r + int(s != 0)
    print(ans)

if __name__ == '__main__':
    main()
