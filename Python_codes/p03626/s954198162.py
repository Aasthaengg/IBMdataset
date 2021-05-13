

def main():
    num = int(input())
    data = [list(input()) for i in range(2)]

    kari = []
    pre = ''

    for i in range(num):
        now_data = data[0][i]
        if pre == '':
            pre = now_data
        elif now_data == pre:
            kari.append(1)
            pre = ''
        else:
            kari.append(0)
            pre = now_data
    if pre != '':
        kari.append(0)

    if kari[0]:
        ans = 6
    else:
        ans= 3
    mod = 10 ** 9 + 7
    pre_kari = kari[0]
    for i in range(1, len(kari)):
        now_kari = kari[i]
        if pre_kari and now_kari:
            ans = (ans * 3) % mod
        elif pre_kari and not now_kari:
            pass
        elif not pre_kari and not now_kari:
            ans = (ans * 2) % mod
        else:
            ans = (ans * 2) % mod
        pre_kari = now_kari


    print(ans % mod)





if __name__ == '__main__':
    main()


