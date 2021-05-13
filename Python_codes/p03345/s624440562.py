#

import sys
input=sys.stdin.readline

def main():
    A,B,C,K=map(int,input().split())
    if K%2==0:
        pm=1
    else:
        pm=-1
    print(pm*(A-B))
    
if __name__=="__main__":
    main()
