#-*-coding:utf-8-*-
import sys
input=sys.stdin.readline

def main():
    n = int(input())
    answers=[]

    if n<=3:
        print(n)
        exit()

    for b in range(2,n):
        #b**2からb**10まで調べる
        for p in range(2,11):
            if b**p > n:
                break
            elif b**p <=n:
                answers.append(b**p)
            else:
                continue
    print(max(answers))
                

if __name__=="__main__":
    main()