# ABC149B

import sys
input=sys.stdin.readline

def main():
    A,B,K=map(int,input().split())
    print(max(A-K,0),max(0,min(A+B-K,B)))
    
    
    
if __name__=="__main__":
    main()
