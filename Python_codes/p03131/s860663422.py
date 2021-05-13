k,a,b = map(int,input().split())
# first
cost = 0
# 2回でb-a枚ふやせる
if b-a <= 2 or k < a-1:
    print(k+1)
else:
    res = a
    k -= a-1
    if k%2 == 1:
        res += 1
        k -=1
    res += (b-a)*(k//2)
    print(res)
