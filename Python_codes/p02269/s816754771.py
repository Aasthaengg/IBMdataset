#coding:utf-8
#1_4_C
n = int(input())
dic = set()
for i in range(n):
    cmd, word = input().split()
    if cmd == "find":
        if word in dic:
            print("yes")
        else:
            print("no")
    else:
        dic.add(word)