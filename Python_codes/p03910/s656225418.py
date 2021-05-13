import sys
N = int(input())
if N == 1:
    print(1)
    sys.exit()

# 数列の和
def re(x):
    return x*(x+1)//2

# 二分探索
l, r = 0, N+1
exact = -1
while abs(l - r) > 1:
    mid = (l + r) // 2
    if re(mid) > N:
        r = mid
    elif re(mid) == N:
        exact = mid
        break
    else:
        l = mid

# 途中抜けしない場合
if exact != -1:
    for i in range(1, exact + 1):
        print(i)

# する場合
else:
    temp = re(r) - N
    for i in range(1, r+1):
        if i != temp:
            print(i)