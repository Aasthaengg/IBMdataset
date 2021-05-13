#

import sys
input=sys.stdin.readline

def main():
    N=int(input())
    S=input()
    maxx=0
    for i in range(1,N+1):
        maxx=max(maxx,S[:i].count("I")-S[:i].count("D"))
    print(maxx)
    
if __name__=="__main__":
    main()
