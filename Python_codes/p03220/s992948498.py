#-*-coding:utf-8-*-
import sys
input=sys.stdin.readline
import decimal

def main():
    numbers=[]
    n = int(input())
    t,a = map(int,input().split())
    numbers=list(map(int,input().split()))
    dp=[]
    hensu=decimal.Decimal('0.006')
    for number in numbers:
        tmp=abs(t-number*hensu-a)
        dp.append(tmp)
    answer=dp.index(min(dp))+1
    print(answer)

if __name__=="__main__":
    main()