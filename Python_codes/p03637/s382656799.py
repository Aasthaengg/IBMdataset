def resolve():
    N = int(input())
    A = list(map(int, input().split()))
    cnt4 = 0
    cnt2 = 0
    _cnt = 0
    for a in A:
        if a % 4 == 0:
            cnt4 += 1
            continue
        if a % 2 == 0:
            cnt2 += 1
            continue
        _cnt += 1
    if cnt2 > 0 and cnt2 % 2 != 0:
        cnt2 -= 1
        _cnt += 1
    print("Yes" if cnt4+1 >= _cnt else "No")




if '__main__' == __name__:
    resolve()