



N = int(input())


def query(idx):
    print(idx)
    s = input()
    if s == "Vacant":
        exit()
    
    return s

base = query(0)

def is_ok(mid):
    s = query(mid)
    # 最初にクエリを投げた場所との差が偶数なので、0~mid間で空席がなければ、midの位置の人は同じ性別になるはず
    if mid % 2 == 0:
        return s == base
    # 偶数の差でないので、midの位置には異なる性別の人が座っているはず、
    else:
        return s != base

lo = 0
hi = N
while hi - lo > 1:
    mid = (hi + lo) // 2
    if is_ok(mid):
        lo = mid
    else:
        hi = mid
