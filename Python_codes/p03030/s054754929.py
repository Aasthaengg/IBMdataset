import sys
from collections import deque


def input():
    return sys.stdin.readline().rstrip()


def main():
    N =int(input())
    l=[]
    for i in range(N):
        k,s = input().split()
        s = int(s)
        l.append([k,s,i+1])



    l.sort(reverse=True)
    mem =""
    q=[]
    for i in range(N):
        k,s,j = l.pop()
        if mem ==k:
            q.append([s,j])
            mem =k
        else:
            q.sort(reverse=True)
            for o,p in q:
                print(p)
            q=[]
            q.append([s, j])
            mem =k
    q.sort(reverse=True)
    if q:
        for o, p in q:
            print(p)






if __name__ == "__main__":
    main()
