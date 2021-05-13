# coding: utf-8

A, B, K = map(int, input().split(" "))

ko_yakusu = []
for i in range(1, 101):
    if (A % i == 0) and (B % i == 0):
        ko_yakusu.append(i)

print(ko_yakusu[-K])
