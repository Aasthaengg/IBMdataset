# -*- coding: utf-8 -*-

import math

op = "init"
ans = []

while (op != "?"):
    a, op, b = input().split()
    a = int(a)
    b = int(b)

    if (op == '+'):
        ans.append(a + b)
    elif (op == '-'):
        ans.append(a - b)
    elif (op == '*'):
        ans.append(a * b)
    elif (op == "/"):
        ans.append(int(a / b))

for answer in ans:
    print(answer)