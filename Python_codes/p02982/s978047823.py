#-*-coding:utf-8-*-
import sys
input=sys.stdin.readline
import itertools
import math
import numpy as np

def main():
    numbers=[]
    #n = int(input())
    n,m = map(int,input().split())
    #numbers=list(map(int,input().split()))
    numbers=np.array([list(map(int,input().split())) for _ in range(n)])
    ans=0
    length=0
    count=0

    for idx,pair in enumerate(itertools.combinations(numbers,2)):
        tmp_A=np.array(pair[0])
        tmp_B=np.array(pair[1])
        length=(tmp_A-tmp_B)**2
        ans=math.sqrt(sum(length))
        if ans.is_integer()==True:
            count+=1
        else:
            continue
    print(count)



if __name__=="__main__":
    main()  