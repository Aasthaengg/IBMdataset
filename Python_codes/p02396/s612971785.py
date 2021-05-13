#coding: UTF-8

def PTC(a):
    for i in range(len(a)):
        if a[i] == "0":
            break
        print("Case "+ str(i+1) +": "+a[i])
        

if __name__=="__main__":
    a = []
    for i in range(10000):
        a.append(input())
        if a[i] == "0":
            break
    PTC(a)