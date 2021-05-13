
def main():
    s = input()
    flg = False
    for i in s:
        if i == '7':
            flg = True
    if flg:
        print('Yes')
    else:
        print('No')


if __name__ == "__main__":
    main()
