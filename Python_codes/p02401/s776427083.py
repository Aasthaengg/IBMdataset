#coding:utf-8
#Simple Calculator

while 1:
    aopb = raw_input().split()
    if aopb[1] == "+":
        print int(aopb[0]) + int(aopb[2])
    elif aopb[1] == "-":
        print int(aopb[0]) - int(aopb[2])
    elif aopb[1] == "*":
        print int(aopb[0]) * int(aopb[2])
    elif aopb[1] == "/":
        print int(aopb[0]) / int(aopb[2])
    else:
        break