#coding:UTF-8
import math
def Count(x):
    if x == 2:
        return 1
    if x<2 or x%2==0:
        return 0
    i=3
    while i<=math.sqrt(x):
        if x%i==0:
            return 0
        i+=2
    return 1

def PN(n,a):
    count=0
    for i in range(n):
        count+=Count(a[i])
    print(count)
    
if __name__=="__main__":
    n=int(input())
    a=[]
    for i in range(n):
        a.append(int(input()))
    PN(n,a)