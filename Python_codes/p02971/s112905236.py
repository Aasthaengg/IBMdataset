#-*-coding:utf-8-*-
import sys
input=sys.stdin.readline
import heapq

def main():
    numbers=[]
    n = int(input())
    [numbers.append(int(input().rstrip())) for _ in range(n)]

    max_n=0
    second_n=0

    for i in numbers:
        if i > max_n:
            max_n=i
        elif i > second_n:
            second_n=i
    
    for i in numbers:
        if i==max_n:
            print(second_n)
        else:
            print(max_n)
    

if __name__=="__main__":
    main()