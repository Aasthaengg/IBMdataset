from collections import defaultdict
s = input()
s = s[::-1]

app = [0 for _ in range(13)]

for i in range(len(s)):
    tmp_dic = [0 for _ in range(13)]
    if i == 0:
        if s[i] != '?':
            tmp_dic[int(s[i])]+= 1
        else:
            for j in range(10):
                tmp_dic[j] += 1

    else:
        if s[i] != '?':
            tmp = int(s[i]) * pow(10, i, 13)
            for j in range(13):
                tmp_dic[(tmp+j)%13] += app[j] % (10**9+7)

        else:
            for j in range(10):
                tmp = int(j) * pow(10, i, 13)
                for k in range(13):
                    tmp_dic[(tmp+k)%13] += app[k] % (10**9+7)

    app = tmp_dic
    # print(app)

print(app[5] % (10**9+7))