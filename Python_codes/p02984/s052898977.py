N = int(input())
A = list(map(int, input().split()))
R = []

'''プラススタート、マイナススタートの累積和を取る'''
plus_start = []
minus_start = []
'''後ろからの累積和'''
plus_start_rev = []
minus_start_rev = []

tmp = 0
pm = -1
for i in range(N):
    pm *= -1
    tmp += A[i] * pm
    plus_start.append(tmp)
tmp = 0
pm = -1
for i in range(-1, -N-1, -1):
    pm *= -1
    tmp += A[i] * pm
    plus_start_rev.append(tmp)

tmp = 0
pm = 1
for i in range(N):
    pm *= -1
    tmp += A[i] * pm
    minus_start.append(tmp)

tmp = 0
pm = 1
for i in range(-1, -N-1, -1):
    pm *= -1
    tmp += A[i] * pm
    minus_start_rev.append(tmp)

'''各山の降水量を計算する'''
for i in range(N):
    if i == 0:
        tmp = plus_start[-1]
        R.append(tmp)
        continue
    if i % 2 == 0:
        tmp = minus_start[i-1] + plus_start_rev[N-i-1]
    else:
        tmp = plus_start[i-1] + minus_start_rev[N-i-1]
    R.append(tmp)

print(*R)
