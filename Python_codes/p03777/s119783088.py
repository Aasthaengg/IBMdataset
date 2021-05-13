# -*- coding: utf-8 -*-
# A - Honest or Dishonest
# 標準入力の取得
a,b = list(input().split())

# 全列挙
char_honest = "H"
char_dishonest = "D"
if a == char_honest:
    if b == char_honest:
        print(char_honest)
    else:
        print(char_dishonest)
else:
    if b == char_honest:
        print(char_dishonest)
    else:
        print(char_honest)