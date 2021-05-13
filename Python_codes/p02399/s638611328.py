#coding: UTF-8

def a_b(a,b):
    print(int(a/b),a%b,format(float(a)/float(b),'.8f'))

if __name__=="__main__":
    a = input().split(" ")
    a_b(int(a[0]),int(a[1]))