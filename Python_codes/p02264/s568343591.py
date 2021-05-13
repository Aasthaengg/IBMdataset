# -*- coding: utf-8 -*-
"""
Created on Tue Jun 20 20:19:33 2017

@author: syaga
"""

if __name__ == "__main__":
    n, q = map(int, input().split())
    a = []
    for i in range(n):
        b = input().split()
        b[1] = int(b[1])
        a.append(b)
    ans = []
    time = 0
    while len(a) != 0:
        x = a.pop(0)
        if x[1] <= q:
            time += x[1]
            ans.append([x[0], time])
        else:
            x[1] -= q
            time += q
            a.append(x)
    for i in ans:
        print(" ".join(map(str, i)))