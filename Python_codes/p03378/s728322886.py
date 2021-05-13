def main():
    _, m, x = map(int, input().split())
    a = {int(an) for an in input().split()}
    cnt_smaller = sum(an < x for an in a)
    print(min(cnt_smaller, m - cnt_smaller))


if __name__ == '__main__':
    main()
