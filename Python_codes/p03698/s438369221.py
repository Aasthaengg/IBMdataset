#

import sys
input=sys.stdin.readline

def main():
    ab="qwertyuiopasdfghjklzxcvbnm"
    S=input()
    y=1
    for a in ab:
        if S.count(a)>1:
            y=0
            break
    if y==1:
        print("yes")
    else:
        print("no")
    
if __name__=="__main__":
    main()
