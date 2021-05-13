#-*-coding:utf-8-*-
import sys
input=sys.stdin.readline

def main():
    s = input().rstrip()
    string_dict={}

    for i in s:
        if i not in string_dict:
            d = {i:1}
            string_dict.update(d) 
        else:
            print("no")
            exit()
    print("yes")

if __name__=="__main__":
    main()