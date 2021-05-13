#-*-coding:utf-8-*-
import sys
input=sys.stdin.readline

def main():
    S = input().rstrip()
    k = int(input())
    
    for i in range(k):
        if S[i]!="1":
            break
    print(S[i])

if __name__=="__main__":
    main()