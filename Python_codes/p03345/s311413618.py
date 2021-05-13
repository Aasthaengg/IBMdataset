#-*-coding:utf-8-*-
import sys
input=sys.stdin.readline

def main():
    a,b,c,k = map(int,input().split())

    if abs(a-b)>10**18:
        print("Unfair")
    elif k % 2==0:
        print(a-b)
    else:
        print(b-a) 

if __name__=="__main__":
    main()