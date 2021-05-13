#-*-coding:utf-8-*-
import sys
input=sys.stdin.readline

def main():
    n = int(input())
    x=[]
    y=[]
    x=list(map(int,input().split()))
    y=list(map(int,input().split()))
    ans=0
    ans_list=[]
    for i in range(1,4):
        for x_value,y_value in zip(x,y):
            ans+=abs(x_value-y_value)**i
            ans_list.append(abs(x_value-y_value))
        print("{:.6f}".format(ans**(1/i)))
        ans=0
    print("{:.6f}".format(max(ans_list)))
    
if __name__=="__main__":
    main()
