#coding: UTF-8
import math

def SC(F):
    for i in range(len(F)):
        ele = F[i].split(" ")
        if ele[1] == "+":
            print(int(ele[0]) + int(ele[2]))
        elif ele[1] == "-":
            print(int(ele[0]) - int(ele[2]))
        elif ele[1] == "*":
            print(int(ele[0]) * int(ele[2]))
        elif ele[1] == "/":
            print(int(int(ele[0]) / int(ele[2])))
        else:
            break
if __name__=="__main__":
    F = []
    for i in range(100000000):
        F.append(input())
        if F[i].split(" ")[1] == "?":
            break
    SC(F)