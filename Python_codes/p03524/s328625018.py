from collections import Counter
S = input()
L = []
for i in range(len(S)):
    L.append(S[i])

c = Counter(L)

if (len(S) == 1):
    print('YES')
    exit()

max_num = 0
min_num = 10**5 + 7
if (len(S) % 2 == 0):
    # 偶数個の場合はlen(S) の切り捨て(含める)までのスライスとそれ以外を[::-1]したのとイコールにならないようにする
    even = 0
    odd = 0
    for i in set(L):
        if (c[i] % 2 == 0):
            even += 1
            max_num = max(max_num, c[i])
            min_num = min(min_num, c[i])
        else:
            odd += 1
            max_num = max(max_num, c[i])
            min_num = min(min_num, c[i])

    if (max_num - min_num > 1):
        print('NO')
        exit()
    else:
        if (even == 3 and odd == 0):
            print('YES')
            exit()
        elif (even == 1 and odd == 2):
            print('YES')
            exit()
        elif (odd == 2 and even == 0):
            print('YES')
            exit()
        else:
            print('NO')
            exit()
else:
    # 奇数この場合はlen(S)の切り捨て(含めない)までのスライスとそれ以外を[::-1]したのとイコールにならないように
    even = 0
    odd = 0
    for i in set(L):
        if (c[i] % 2 == 0):
            even += 1
            max_num = max(max_num, c[i])
            min_num = min(min_num, c[i])
        else:
            odd += 1
            max_num = max(max_num, c[i])
            min_num = min(min_num, c[i])
    if (max_num - min_num > 1):
        print('NO')
        exit()
    else:
        if (even == 2 and odd == 1):
            print('YES')
            exit()
        elif (even == 0 and odd == 3):
            print('YES')
            exit()
        else:
            print('NO')
            exit()
