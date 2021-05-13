#-*-coding:utf-8-*-
import sys
input=sys.stdin.readline

def main():
    exams=[]
    sorted_exams=[]
    n = int(input())
    exams=list(map(int,input().split()))
    sorted_exams=sorted(exams)
    half=n//2

    start=sorted_exams[half-1]
    end=sorted_exams[half]

    print(end-start)

if __name__=="__main__":
    main()