#! /usr/bin/env python
# -*- coding: utf-8 -*-

''' ???????????? '''

# pop???push??¨??????????????????????????????????????????????????¨??£??\????????????????????????
# ?¨??????????O(1)


operators = {"+": lambda x, y: x + y,
             "-": lambda x, y: x - y,
             "*": lambda x, y: x * y,
             "/": lambda x, y: x / y}


def compute(A):
    stack = []

    for i in range(len(A)):
        # ?????????
        if isinstance(A[i], str):
            op_right = stack.pop()
            op_left = stack.pop()
            # ?¨???????????????????????????????
            stack.append(operators[A[i]](op_left, op_right))

        # ???????????????
        if isinstance(A[i], int):
            stack.append(A[i])

    return stack[-1]

if __name__ == '__main__':
    A = list(input().split())
    # A = list("1 2 + 3 4 - *".split())

    for i in range(len(A)):
        if not A[i] in ['+', '-', '*', '/']:
            A[i] = int(A[i])

    print(compute(A))