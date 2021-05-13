S = input()

alpha = 'abcdefghijklmnopqrstuvwxyz'
# len(S)が26未満の場合
if len(S) < 26:
    for char in alpha:
        # Sに入っていない文字の中で最小のものを末尾に足す
        if char not in S:
            print(S + char)
            exit()

# len(S)が26の場合
else:
    arr = [S[-1]]

    for i in range(1, 26):
        l = 25 - i
        if max(arr) > S[l]:
            chars = []

            for c in arr:
                # 下のifがよくわかってない
                # bcdefghijklmnopqrstuvwx | zya　みたいな時のため？
                # ifがないと~~~vwa とか吐いて前に戻ってしまうっぽい
                # 時間内に思いつく気が全くしない
                if c > S[l]:
                    chars.append(c)
            char = min(chars)
            # print(chars)

            # for c in arr:
            #     chars.append(c)
            # char = min(chars)

            print(S[:l] + char)
            exit()
        else:  # max(sr)>S[l]　の場合
            arr.append(S[l])

    print(-1)
