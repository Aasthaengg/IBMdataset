#coding: UTF-8

def Rectangle(a,b):
    return a*b,2*(a+b)

if __name__=="__main__":
    a = input().split(" ")
    area,length = Rectangle(int(a[0]),int(a[1]))
    print(area,length)