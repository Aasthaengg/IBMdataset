
def main():
    k = int(input())
    a, b = map(int, input().split())
    flg = False
    for i in range(a, b+1):
        if i % k == 0:
            print('OK')
            flg = True
            break
    if not flg:
        print('NG')


if __name__ == "__main__":
    main()
