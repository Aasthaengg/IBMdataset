#-*-coding:utf-8-*-
import sys
input=sys.stdin.readline

def main():
    strings=[]
    h,w = map(int,input().split())
    strings=[input().rstrip() for _ in range(h)]
    output=""

    for i in range(h+2):
        if i==0 or i==h+1:
            igeta="#"*(w+2)
            print("{}".format(igeta))
        else:
            output="#"+strings[i-1]+"#"
            print(output)

if __name__=="__main__":
    main()