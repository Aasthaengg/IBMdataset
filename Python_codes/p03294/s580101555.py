#-*-coding:utf-8-*-
import sys
input=sys.stdin.readline

def main():
    number = int(input())
    numbers=[]
    numbers=list(map(int,input().split()))
    answer=0
    for i in numbers:
        answer+=i-1
    print(answer)

if __name__=="__main__":
    main()