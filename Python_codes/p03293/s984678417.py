#-*-coding:utf-8-*-
import sys
input=sys.stdin.readline

def main(): 
    s = list(input().rstrip())
    t = input().rstrip()
    for i in range(len(s)):
        if t == "".join(s):
            print("Yes")
            exit()
        else:
            tmp=s.pop(0)
            s.append(tmp)
    print("No")



if __name__=="__main__":
    main()