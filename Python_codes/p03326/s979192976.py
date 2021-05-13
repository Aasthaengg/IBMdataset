import sys

def resolve():
    N, M = list(map(int, input().split()))
    XYZ = [list(map(int, input().split())) for _ in range(N)]
    ans = 0
    for bits in range(1<<3):
        coef = [-1, -1, -1]
        for odr in range(3):
            if bits & (1<<odr):
                coef[odr] = 1
        _XYZ = sorted(XYZ, key=lambda x: coef[0]*x[0]+coef[1]*x[1]+coef[2]*x[2], reverse=True)
        totals = [0, 0, 0]
        for i in range(M):
            totals[0] += _XYZ[i][0]
            totals[1] += _XYZ[i][1]
            totals[2] += _XYZ[i][2]
        ans = max(ans, sum(map(abs, totals)))
    print(ans)

if '__main__' == __name__:
    resolve()