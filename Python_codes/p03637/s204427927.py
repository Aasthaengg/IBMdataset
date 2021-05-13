
def main():
    n = int(input())
    a = list(map(int, input().split()))
    div2 = 0
    div4 = 0
    notdiv4 = 0
    for ea in a:
        if ea % 4 == 0:
            div4 += 1
        elif ea % 2 == 0:
            div2 += 1
        else:
            notdiv4 += 1

    notdiv4 += div2 % 2
    if notdiv4 - 1 > div4:
        print('No')
    else:
        print('Yes')

if __name__ == '__main__':
    main()