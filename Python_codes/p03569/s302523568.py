s = input()

ans = 0

while s:

    # 先頭と末尾が同じ場合
    if s[0] == s[-1]:
        s = s[1:-1]

    ##### 以下、先頭と末尾が異なる場合の分類 #####

    # 先頭がxの場合
    elif s[0] == 'x':
        # 仮想的に末尾にxを足す
        s = s[1:]
        ans += 1

    # 末尾がxの場合
    elif s[-1] == 'x':
        # 仮想的に先頭にxを足す
        s = s[:-1]
        ans += 1

    # 先頭も末尾もxではない場合
    else:
        print(-1)
        exit()

print(ans)