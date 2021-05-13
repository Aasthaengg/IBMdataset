#キーエンスプログラミングコンテスト2019-B
s = input()

target = 'keyence'
flg = False
for i in range(len(s)):
    for j in range(len(s)):
        tmp = s[0:i] + s[j:]
        if tmp == target and not flg:
            print('YES')
            flg = True
            break
if not flg:
    print('NO')