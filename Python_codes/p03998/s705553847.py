#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# FileName: 	B
# CreatedDate:  2020-07-16 23:00:42 +0900
# LastModified: 2020-07-16 23:23:14 +0900
#
from collections import deque


def main():
    s_a = input()
    s_b = input()
    s_c = input()
    s_a = [s for s in s_a if s != 'a']
    s_b = [s for s in s_b if s != 'b']
    s_c = [s for s in s_c if s != 'c']
    s_a = deque(s_a)
    s_b = deque(s_b)
    s_c = deque(s_c)
    if not s_a:
        print("A")
        return
    turn = s_a.popleft()
    ans = -1
    while 1:
        if turn == 'a' and s_a:
            turn = s_a.popleft()
        elif turn == 'b' and s_b:
            turn = s_b.popleft()
        elif turn == 'c' and s_c:
            turn = s_c.popleft()
        elif turn == 'a' and not s_a:
            ans = 0
            break
        elif turn == 'b' and not s_b:
            ans = 1
            break
        elif turn == 'c' and not s_c:
            ans = 2
            break
    if ans == 0:
        print("A")
    elif ans == 1:
        print("B")
    else:
        print("C")
    return




if __name__ == "__main__":
    main()
