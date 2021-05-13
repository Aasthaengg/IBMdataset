import math
import collections
import fractions
import itertools
import functools
import operator

def solve():
    n = int(input())
    s = input()
    ans = 0
    hoge = [ans]
    for i in s:
        if i == "I":
            ans += 1
        else:
            ans -= 1
        hoge.append(ans)
    print(max(hoge))
    return 0

if __name__ == "__main__":
    solve()