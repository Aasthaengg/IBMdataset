import math
N, A, B = map(int, input().split())

H = [int(input()) for _ in range(N)]


H.sort(reverse=True)
high = math.ceil(H[0] / B)
low = 0
while high > low+1:
    mid = (high+low) // 2
    cnt = 0
    for i in range(N):
        if H[i] - mid*B > 0:
            # 残りを減らすのに必要な回数を計上
            cnt += math.ceil((H[i] - mid*B)/(A - B))
        else:
            break
    # 残りを減らす回数がmidを超えているならその回数ではすべてを倒しきれない
    if cnt <= mid:
        high = mid
    else:
        low = mid

print(high)