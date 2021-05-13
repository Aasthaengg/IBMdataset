# -*- coding: utf-8 -*-
# 整数の入力
#a = int(input())
# スペース区切りの整数の入力

lists=list(map(int,input().split()))
# 文字列の入力
#s = input()
# 出力
#print("{} {}".format(a+b+c, s))

#cがa以上かつb以下
if lists[0]<=lists[2] and lists[1]>=lists[2]:
        print("Yes")
else:
    print("No")
