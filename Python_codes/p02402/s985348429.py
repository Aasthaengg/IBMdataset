#coding: UTF-8
import math

def MMS(n,a):
    min = max = int(a[0])
    sum = int(a[0])
    for i in range(1,n):
        if min > int(a[i]):
            min = int(a[i])
        if max < int(a[i]):
            max = int(a[i])
        sum += int(a[i])
    print(min,max,sum)
    
if __name__=="__main__":
    n = int(input())
    a = input().split(" ")
    MMS(n,a)    