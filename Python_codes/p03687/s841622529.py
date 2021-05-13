from string import ascii_lowercase

S = list(input())

ans = 10 ** 18
# 全てのアルファベットを試す
for moji in ascii_lowercase:
    tmp = S[:]
    count = 0
    while len(set(list(tmp))) != 1:
        for i in range(len(tmp) - 1):
            if tmp[i] == moji or tmp[i + 1] == moji:
                tmp[i] = moji
        tmp = tmp[:-1]
        count += 1
    ans = min(ans, count)
print(ans)

