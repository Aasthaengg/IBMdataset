
from math import factorial

def combinations_count(n, r):
    return factorial(n) // (factorial(n - r) * factorial(r))

def main():
    num = int(input())
    data = list(map(int, input().split()))

    ketasuu = 20
    righ = 0

    keta_flg = [0 for i in range(ketasuu)]
    ans = 0


    for left in range(num):

        left_bin = bin(data[left])[2:]
        left_bin = left_bin.zfill(ketasuu)

        for i in range(ketasuu):
            if left_bin[i] == '1':
                keta_flg[i] = 1

        righ = max(righ, left + 1)

        while righ < num:
            righ_bin = bin(data[righ])[2:]
            righ_bin = righ_bin.zfill(ketasuu)

            flg = 0
            for i in range(ketasuu):
                if righ_bin[i] == '1' and keta_flg[i]:
                    flg = 1
                    break

            if flg:
                break

            for i in range(ketasuu):
                if righ_bin[i] == '1':
                    keta_flg[i] = 1

            righ += 1

        ans += righ - left


        for i in range(ketasuu):
            if left_bin[i] == '1':
                keta_flg[i] = 0

    print(ans)






if __name__ == '__main__':
    main()