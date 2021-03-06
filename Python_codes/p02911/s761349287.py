#-*-coding:utf-8-*-
import sys
input=sys.stdin.readline
import numpy as np

def main():
    n,k,q = map(int,input().split())
    points=np.array([k]*n)
    i=0
    while i < q:
        point=int(input().rstrip())
        points-=1
        points[point-1]+=1
        i+=1
    for data in points:
        if data > 0:
            print("Yes")
        else:
            print("No")
if __name__=="__main__":
    main()