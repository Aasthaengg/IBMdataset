#-*-coding:utf-8-*-
import sys
input=sys.stdin.readline

def main():
    s = input()
    if s[0]!="A":
        print("WA")
        exit()
    if s[2:-2].count('C')!=1:
        print("WA")
        exit()
    s=s.replace('A','')
    s=s.replace('C','')
    if s.islower()==False:
        print("WA")
        exit()
    else:
        print("AC")


if __name__=="__main__":
    main()