#

import sys
input=sys.stdin.readline

def main():
    H,W=map(int,input().split())
    print("".join(["#"]*(W+2)))
    for i in range(H):
        print("#",input().strip("\n"),"#",sep="")
    print("".join(["#"]*(W+2)))
    
if __name__=="__main__":
    main()
