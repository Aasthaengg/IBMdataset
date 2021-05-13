def main():
    n = int(input())
    A = [int(x) for x in input().split()]
    flag = True
    for a in A:
        if a % 2 != 0:
            continue
        else:
            if a % 3 != 0 and a % 5 != 0:
                flag = False
    if flag:
        print('APPROVED')
    else:
        print('DENIED')

if __name__ == '__main__':
    main()