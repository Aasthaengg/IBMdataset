# -*- coding: utf-8 -*-
# スペース区切りの整数の入力
a, b, c = map(int, input().split())

numberList = [a,b,c]
numberList.sort()
[A,B,C]=numberList

if A==B and B==C:
    print("Yes")
else:
    print("No")