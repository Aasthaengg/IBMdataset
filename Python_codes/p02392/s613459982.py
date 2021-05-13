# coding: utf-8

num = input().rstrip().split(" ")

if (int(num[0]) < int(num[1]) and int(num[1]) < int(num[2])):
    print("Yes")
else:
    print("No")