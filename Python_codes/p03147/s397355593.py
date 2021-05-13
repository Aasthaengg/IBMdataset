n = int(input())
h_list = list(map(int, input().split()))

# 高さが小さいものの方が早く目標に到達する
# どの花も目標に到達していないときは全てをプラス1
# 到達した花がある場合はそれを基準に2つに分け、同様に作業をする
count = 0
while True:
    if (n == 0):
        break
    p = 0
    check = 0
    for i in range(n):
        if (i == 0 and h_list[i] == 0):
            h_list.pop(i)
            # 数えたくないbreakよりcheckを増やし、あとでcountをcheckで引く
            check += 1
            n -= 1
            break
        elif (h_list[i] != 0):
            if (h_list[i] > 0):
                h_list[i] -= 1

        elif (i != 0 and h_list[i] == 0):
            break

    p += 1
    count += p
    count -= check

print(count)
