#-*-coding:utf-8-*-
import sys
input=sys.stdin.readline

def main():
    strings = input()
    answers=[]
    counter=0

    for string in strings:
        if "A" in string or "C" in string or "G" in string or "T" in string:
            counter+=1
        else:
            answers.append(counter)
            counter=0
    print(max(answers))


if __name__=="__main__":
    main()