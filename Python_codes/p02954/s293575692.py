import math
import collections
import fractions
import itertools

def solve():
    s = input()
    n = len(s)
    ans = [0]*n
    cnt = 0
    for i, moji in enumerate(s):
        if moji == "R":
            cnt += 1
            continue
        else:
            even_num = cnt//2
            odd_num = cnt - even_num
            ans[i] += even_num
            ans[i-1] += odd_num
            cnt = 0
    for i in range(n-1, -1, -1):
        if s[i] == "L":
            cnt += 1
            continue
        else:
            even_num = cnt // 2
            odd_num = cnt - even_num
            ans[i] += even_num
            ans[i+1] += odd_num
            cnt = 0
    print(*ans)
    return 0

if __name__ == "__main__":
    solve()
