# B - Buffet
def main():
    _ = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = list(map(int, input().split()))
    cnt = 0
    flg = a[0]

    for i in a:
        if flg == i - 1:
            cnt += c[flg-1]
        cnt += b[i-1]
        flg = i
    print(cnt)

if __name__ == '__main__':
    main()