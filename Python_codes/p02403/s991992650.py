#coding: UTF-8
import math

def PR(a):
    for k in range(len(a)):
        area = ""
        H = int(a[k].split(" ")[0])
        W = int(a[k].split(" ")[1])
        if H == 0 and W == 0:
            break
        for j in range(H):
            for i in range(W):
                area += "#"
            print(area)
            area = ""
        print("")

if __name__=="__main__":
    a = []
    for i in range(300):
        a.append(input())
        if a[i] == "0 0":
            break
    PR(a)  