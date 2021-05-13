#

import sys
input=sys.stdin.readline

def main():
    N=int(input())
    S=input().strip("\n")
    if N%2==1:
        print("No")
    elif S[:(N//2)]==S[(N//2):]:
        print("Yes")
    else:
        print("No")
    
    
    
if __name__=="__main__":
    main()
