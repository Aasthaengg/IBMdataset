N, x = map(int, input().split())
As = list(map(int, input().split()))

# 隣り合う箱の和を取る
# sum_As = [0 for i in range(N-1)]
# for i in range(N-1):
#     sum_As[i] = As[i] + As[i+1]

count = 0
# 両側があふれていたら減らせるだけ減らそう
for i in range(1, N-1):
    if As[i-1]+As[i] > x and As[i]+As[i+1] > x:
        minus = min(As[i], As[i-1]+As[i]-x, As[i]+As[i+1]-x)
        As[i] -= minus
        count += minus

# 片側があふれていたら減らせるだけ減らそう
if As[0]+As[1] > x:
    minus = min(As[0], As[0]+As[1]-x)
    As[0] -= minus
    count += minus

for i in range(1, N-1):
    if As[i-1]+As[i] > x:
        minus = min(As[i], As[i-1]+As[i]-x)
        As[i] -= minus
        count += minus
    if As[i]+As[i+1] > x:
        minus = min(As[i], As[i]+As[i+1]-x)
        As[i] -= minus
        count += minus

if As[N-2]+As[N-1] > x:
    minus = min(As[N-1], As[N-2]+As[N-1]-x)
    As[N-1] -= minus
    count += minus

print(count)
