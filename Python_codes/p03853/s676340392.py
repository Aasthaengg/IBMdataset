#-*-coding:utf-8-*-
import sys
input=sys.stdin.readline
import numpy as np

def main():
    dot=[]
    h,w = map(int,input().split())
    dot=np.array([list(input().rstrip()) for _ in range(h)])
    
    for i in range(1,h+1):
        print("".join(dot[i-1]))
        print("".join(dot[int(i+1/2)-1]))

if __name__=="__main__":
    main()