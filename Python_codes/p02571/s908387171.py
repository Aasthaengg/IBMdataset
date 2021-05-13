# coding: utf-8
# Your code here!

#検索される文字列
S = input()
#検索する文字列
T = input()
min = len(T)


for Snum in range(len(S)- len(T) + 1):
    count = 0
    for i in range(len(T)):
        if S[Snum + i] != T[i]:
            count += 1
    if count < min:
        min = count
print(min)