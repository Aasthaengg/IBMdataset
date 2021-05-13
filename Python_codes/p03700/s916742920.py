import math
N, A, B = map(int, input().split())
H = [int(input()) for _ in range(N)]

OK = max(H)//B+1
NG = 0

ans = OK
while OK-NG > 1:
    mid = (OK+NG)//2  # 試行する値
    cnt = 0

    for h in H:
        if h > mid*B:
            cnt += math.ceil((h-mid*B)/(A-B))

    if cnt <= mid:
        OK = mid
    else:
        NG = mid

print(OK)
