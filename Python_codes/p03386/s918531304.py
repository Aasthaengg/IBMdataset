#-*-coding:utf-8-*-
import sys
input=sys.stdin.readline
import numpy as np

def main2():
    A,B,K=map(int,input().split())
    if A+K-1>=B-K+1:
        for i in range(A,B+1):
            print(i)
    else:
        for i in range(A,A+K):
            print(i)
        for i in range(B-K+1,B+1):
            print(i)

def main():
    numbers=[]
    a,b,k = map(int,input().split())
    numbers=np.arange(a,b+1)
    A=set(numbers[:k])
    B=set(numbers[-k:])
    answers = A|B
    
    for i in sorted(answers):
        print(i)

if __name__=="__main__":
    main2()