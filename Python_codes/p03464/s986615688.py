



K = int(input())

A = list(map(int, input().split()))


if A[-1] != 2:
    print(-1)
    exit()

big = 2
small = 2
for i in reversed(range(K)):
    """
    smallのときにai人組つくると脱落者なし
    bigのときにai人組作るとai-1人脱落

    """


    # smallは元のsmall以上かつ、脱落者なし
    """
    ・smallはaiで割り切れる（脱落者なし）
    ・元のsmall以上の値
    """

    if small // A[i] > 0 and small % A[i] > 0:
        small = (small // A[i] + 1) * A[i]
    elif small // A[i] > 0 and small % A[i] == 0:
        pass
        #small = small
    elif small // A[i] == 0:
        small = A[i] 
        
    # bigは元のbig以上かつ、脱落者がai-1
    big = (big // A[i]) * A[i] + A[i] - 1

    if big < small:
        print(-1)
        exit()


print(small, big)
