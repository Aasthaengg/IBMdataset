#-*-coding:utf-8-*-
import sys
input=sys.stdin.readline

def main():
    cards=[]
    sorted_cards=[]
    n = int(input())
    cards=list(map(int,input().split()))
    sorted_cards=sorted(cards,reverse=True)
    alice=0
    bob=0

    for idx,card in enumerate(sorted_cards):
        if idx%2==0:
            alice+=card
        else:
            bob+=card
    print(alice-bob)

if __name__=="__main__":
    main()