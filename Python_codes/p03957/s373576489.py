def main():
    S = list(input())
    flag = False
    for s in S:
        if s == 'C':
            flag = True
        else:
            pass
        if flag and s == 'F':
            print('Yes')
            break
    else:
        print('No')


if __name__ == '__main__':
    main()
