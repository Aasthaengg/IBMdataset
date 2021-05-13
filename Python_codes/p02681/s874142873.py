def main():
    s = input().rstrip()
    t = input().rstrip()

    s_len = len(s)
    t_len = len(t)
    if s_len+1 == t_len and s == t[:s_len]:
        print('Yes')
    else:
        print('No')


if __name__ == '__main__':
    main()
