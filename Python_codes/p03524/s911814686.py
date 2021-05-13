import math
import collections
import fractions
import itertools
import functools
import operator

def solve():
    s = list(input())
    a = s.count("a")
    b = s.count("b")
    c = s.count("c")
    hoge = [a, b, c]
    for i in range(2):
        if abs(hoge[i] - hoge[i+1]) > 1 or abs(hoge[0] - hoge[2]) > 1:
            print("NO")
            break
    else:
        print("YES")
    return 0

if __name__ == "__main__":
    solve()
