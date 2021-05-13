import bisect
def resolve():
    A, B, Q = list(map(int, input().split()))
    S = [int(input()) for _ in range(A)]
    T = [int(input()) for _ in range(B)]
    X = [int(input()) for _ in range(Q)]
    #print("#####")
    for x in X:
        ans = float("inf")
        for Ary1, Ary2 in [[S, T], [T, S]]:
            ar1_nearests = get_nearest_pos(Ary1, x)
            for p in ar1_nearests:
                ar2_nearests = get_nearest_pos(Ary2, p)
                for p2 in ar2_nearests:
                    ans = min(ans, abs(x-p)+abs(p-p2))
        print(ans)

def get_nearest_pos(array, pos):
    res = []
    idx = bisect.bisect_left(array, pos)
    if idx == 0:
        res.append(array[idx])
    elif idx == len(array):
        res.append(array[idx-1])
    else:
        res.append(array[idx])
        res.append(array[idx-1])
    return res


if '__main__' == __name__:
    resolve()