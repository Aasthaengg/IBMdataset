import math

n,k = (int(x) for x in input().split())
w = list()

for i in range(0, n):
    w.append(int(input()))

def check(P):
    i = 0
    for j in range(0, k):
        summ = 0
        while(summ + w[i] <= P):
            summ += w[i]
            i += 1
            if(i == n): #最後までしまえたら終了
                return n

    return i #入りきらなかったら終了

def Binary_Search():
    left = 0
    right = 100000*100000
    while(right - left > 1):
        mid = math.floor((left + right) / 2)
        if(check(mid) >= n): #全部トラックに入ったなら範囲の最大値をを狭める
            right = mid
        else:
            left = mid

    return right

ans = Binary_Search()

print(ans)

