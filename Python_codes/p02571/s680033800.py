# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！

a = input()
b = input()

s = 1001

for i in range(len(a) - len(b)+ 1):
    score = 0
    test = a[i:i+len(b)]
    for j in range(len(b)):
        if test[j] != b[j]:
            score += 1
    s = min(s, score)

print(s)