K, A, B = map(int, input().split())
# 1円に交換するためにはA枚のビスケットがいる　操作１
# B枚のビスケットにするためには1円がいる　操作２
# 持っているビスケット(０個でもいい)を叩けば一個ビスケットが得られる　操作３

# A > B
# A == B
# A < B

if (K == 1):
    print(K + 1)
    exit()

if (A >= B):
    print(K + 1)
    exit()

elif (A < B):
    # 1円を作るたびに操作３を実行
    nokori = K - (A - 1)
    bis = A
    for _ in range(A):
        if (nokori % 2 != 0):
            nokori -= 1
            bis += 1
        else:
            break

    if (bis + ((B - A) * (nokori // 2)) >= 1 + K):
        print(bis + ((B - A) * (nokori // 2)))
    else:
        print(1 + K)
