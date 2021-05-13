#-*-coding:utf-8-*-
import sys
input=sys.stdin.readline

def main():
    data=[]
    n = int(input())
    k = int(input())
    data=list(map(int,input().split()))
    length=0

    for ball in data:
        if ball < k-ball:
            length+=2*ball
        else:
            length+=2*(k-ball)
    print(length)

if __name__=="__main__":
    main()