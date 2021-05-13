#ALDS1_4_D Allocaion
def check(k, w, p):  # 積載制限 p 台数 k のトラックに乗り切るか確認
    j = 0
    for i in range(k):
        sum = 0
        while sum < p:
            if sum + w[j] > p:
                break
            else:
                sum += w[j]
                j += 1
            if j == len(w):  # 積載完了
                break
        if j == len(w):
            break

    if j == len(w):
        return True
    else:
        return False


n, k = map(int, input().split())
w = [int(input()) for _ in range(n)]

left = sum(w) // k - 1
right = left + max(w)

while True:
    mid = (left + right) // 2
    # print('mid : {}'.format(mid))

    if check(k, w, mid):
        right = mid
    else:
        left = mid
    if right - left <= 1:
        break
    # print('left : {}  right : {}'.format(left, right))

print(right)

