from collections import Counter

N = int(input())
A = list(map(int, input().split()))

c = Counter(A)

# 帽子の種類数を取得する
c_set = set(A)

# 帽子の種類数が1個の時、数値が0なら条件を満たす
if len(c_set) == 1:
    if c[0] != 0:
        print('Yes')
        exit(0)

# 帽子の種類数が2個の時、数値が0の帽子がN/3なら条件を満たす
elif len(c) == 2:
    if c[0] == N//3:
        print('Yes')
        exit(0)

# 帽子の種類数が3個の時、x^y^z=0で条件を満たす
elif len(c) == 3:
    check = -1
    check_list = []
    for a in c_set:
        check_list.append(a)
        if check == -1:
            check = c[a]
        else:
            if check != c[a]:
                print('No')
                exit(0)

    # 同じ個数ずつあった時に、x^y^z=0であるか
    if check_list[0] ^ check_list[1] ^ check_list[2] == 0:
        print('Yes')
        exit(0)
print('No')
