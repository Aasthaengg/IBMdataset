#-*-coding:utf-8-*-
import sys
input=sys.stdin.readline

def main():
    a,b,c = map(int,input().split())
    count=0

    if a % 2 ==1 and b % 2 ==1 and c % 2 ==1:
        print(count)
        exit()

    while True:
        if a == b ==c:
            print(-1)
            exit()
        elif a % 2 ==0 and b % 2==0 and c % 2 ==0:
            tmp_a=a/2
            tmp_b=b/2
            tmp_c=c/2
            a=tmp_b+tmp_c
            b=tmp_a+tmp_c
            c=tmp_b+tmp_a
            count+=1
        else:
            break
    print(count)

if __name__=="__main__":
    main()