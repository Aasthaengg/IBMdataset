from functools import lru_cache
import sys

sys.setrecursionlimit(1000000)

N = int(input())

def cnt_power(ans, n, cnt):
    if cnt>n:
        return ans
    elif (ans*cnt) >= (10**9+7) :
        ans = ans*cnt % (10**9+7)
        cnt += 1
        return cnt_power(ans, n, cnt)
    else:
        ans = ans*cnt
        cnt += 1
        return cnt_power(ans, n, cnt)

print(cnt_power(1, N, 1))