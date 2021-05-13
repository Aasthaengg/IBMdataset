import sys
def input(): return sys.stdin.readline().rstrip()
from itertools import combinations
from collections import Counter
def main():
    n=int(input())
    if n==1:
        print(1)
        sys.exit()
    XY=[tuple(map(int,input().split())) for i in range(n)]
    XY.sort()
    lis=list(combinations(XY,2))
    PQ=[]
    for l in lis:
        PQ.append((l[1][0]-l[0][0],l[1][1]-l[0][1]))
    x=Counter(PQ).most_common(1)[0][1]
    print(n-x)

if __name__=='__main__':
    main()