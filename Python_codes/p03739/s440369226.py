# -*- coding: utf-8 -*-
def calc(flag):
    s = res = 0
    for i in range(N):
        flag = flag * -1
        s += a[i]
        if flag == 1:
            if s <= 0:
                res += abs(s) + 1
                s = 1
        elif flag == -1:
            if s >= 0:
                res += abs(s) + 1
                s = -1
    return res

N = int(input())
a = list(map(int, input().split()))

ans = min(calc(1), calc(-1))
print(ans)
