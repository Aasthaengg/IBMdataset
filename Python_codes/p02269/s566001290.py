from sys import stdin
import sys
input = stdin.readline

dic = {}
n = int(input())
for i in range(n):
    s = input()
    if s[0] == 'i':
        dic[s[7:]] = 1
    else:
        print("yes" if s[5:] in dic else "no")

