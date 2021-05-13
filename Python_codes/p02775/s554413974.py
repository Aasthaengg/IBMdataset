# e 数位dp 还可以从右到左
# 参考 https://maspypy.com/atcoder-%e5%8f%82%e5%8a%a0%e6%84%9f%e6%83%b3-2019-02-16abc-155
# https://atcoder.jp/contests/abc155/submissions/10155415
# in your code
import numpy as np
DBG=0
def p(*args, **kargs):
    if DBG:print(*args, **kargs)
read = input 
rn = lambda :list(map(int, read().split()))

def sol(s):
    dp = 0, 1 # n, n + 1
    for x in map(int, s):
        c, d = dp
    #                     为什么这里x = 0的时候不受影响 c+0 << d+10，因为abs(c-d) < 1
        
        #    前一位没借位  前一位借位
        a = min(c + x,    d + 10 - x)# for ...n
        #    这里x=9为什么不受影响, c+10 >> d，因为abs(c-d) < 1
        b = min(c + x + 1,d + 10 - 1 - x )# for ...(n+1)
        
        # 因为a,b相差小于1。f(n), f(n+1)相差总是小于1，多给1元即可
        dp = a,b
        p(dp)
    return dp[0]
if DBG:
    pass
#     sol("100")
#     assert 8 == sol("36")
#     assert sol("91") == 3
#     assert 243 == sol("314159265358979323846264338327950288419716939937551058209749445923078164062862089986280348253421170")
print(sol(read()))