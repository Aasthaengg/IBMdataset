#coding: UTF-8

def HMD(a,b,c):
    counter = 0
    for i in range(a,b+1):
        if c%i == 0:
            counter += 1
    print(counter)

if __name__=="__main__":
    a = input().split(" ")
    HMD(int(a[0]),int(a[1]),int(a[2]))