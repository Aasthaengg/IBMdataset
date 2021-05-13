h,w,k = map (int,input().split())
s = [0] * h
aans =10000000
for i in range(h):
    s[i] = [int(i) for i in str(input())]
for i in range(2 ** (h - 1)):
    ans = 0

    kugiri = [0] * (h - 1)
    for j in range(h - 1):  # このループが一番のポイント
        if ((i >> j) & 1):  # 順に右にシフトさせ最下位bitのチェックを行う
            kugiri[j] = 1

    box = [0] * (sum(kugiri) + 1)
    ans += sum(kugiri)
    for j in range(w): #横に見てる
        
        box[0] += s[0][j]
        num = 0
        for l in range(1,h): #縦に足し合わせる
            num += kugiri[l-1]

            box[num] = s[l][j] + box[num]

        for l in range(len(box)):
            if box[l] > k and j != 0:
                box = [0 for _ in range(sum(kugiri) + 1)]
                num = 0
                box[0] += s[0][j]
                for m in range(1, h):
                    num += kugiri[m - 1]
                    box[num] = s[m][j] + box[num]
                ans += 1
                break
            elif box[l] > k and j == 0:
                ans += 10000000000

    aans =min(aans,ans)


print(aans)


