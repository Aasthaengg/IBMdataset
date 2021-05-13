#coding: UTF-8

def Swap(a):
    for i in range(len(a)):
        if a[i] == "0 0":
            break
        x = int(a[i].split(" ")[0])
        y = int(a[i].split(" ")[1])
        box = 0
        if x > y:
            box = x
            x = y
            y = box
        print(str(x)+" "+str(y))

if __name__=="__main__":
    a = []
    for i in range(3000):
        a.append(input())
        if a[i] == "0 0":
            break
    Swap(a)