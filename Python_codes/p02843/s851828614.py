#-*-coding:utf-8-*-
import sys
input=sys.stdin.readline

def main():
    X = int(input())
    C = X // 100
    if X >= C * 100 and X <= C * 105:
        print(1)
    else:
        print(0)

if __name__=="__main__":
    main()