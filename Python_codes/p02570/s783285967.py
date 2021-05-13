#coding:utf-8

input_line = input().split(" ")
D = int(input_line[0])
T = int(input_line[1])
S = int(input_line[2])

if D/S <= T:
    print("Yes")
else:
    print("No")