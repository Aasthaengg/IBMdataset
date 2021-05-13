import sys
from itertools import groupby
def input(): return sys.stdin.readline().rstrip()


def main():
    S=list(input())
    ans=[0]*(len(S))
    index=0
    for key, value in groupby(S):
        le=len(list(value))
        if key=='L':
            ans[index]+=(le+1)//2
            ans[index-1]+=le//2
        else:
            ans[index+le]+=le//2
            ans[index+le-1]+=(le+1)//2
        index+=le
    print(*ans, sep=" ")
    


if __name__ == '__main__':
    main()