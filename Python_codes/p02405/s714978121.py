#coding: UTF-8
import math

def PC(a):
    for k in range(len(a)):
        area = ""
        H = int(a[k].split(" ")[0])
        W = int(a[k].split(" ")[1])
        if H == 0 and W == 0:
            break
        for j in range(H):
            if j%2 == 0:
                for i in range(W):
                    if i%2 == 0:
                        area += "#"
                    else :
                        area += "."
            else :
                for i in range(W):
                    if i%2 == 0:
                        area += "."
                    else:
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
    PC(a)    