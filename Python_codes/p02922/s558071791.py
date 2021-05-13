#-*-coding:utf-8-*-
import sys
input=sys.stdin.readline

def main():
    a,b = map(int,input().split())
    plug=1
    ans=0

    while True:
        if plug >= b:
            break
        plug+=a-1
        ans+=1
#        print("count={},plug={}".format(count,plug))
    print(ans)

if __name__=="__main__":
    main()