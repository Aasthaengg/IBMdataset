#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# FileName: 	B
# CreatedDate:  2020-07-29 16:31:41 +0900
# LastModified: 2020-07-29 16:49:31 +0900
#


def main():
    S = sorted(input())
    T = sorted(input(), reverse=True)
    sorted_S = ""
    sorted_T = ""
    for s in S:
        sorted_S += s
    for t in T:
        sorted_T += t
    if sorted_S < sorted_T:
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()
