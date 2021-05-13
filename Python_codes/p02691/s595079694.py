import sys
import numpy as np
from collections import defaultdict



input = sys.stdin.readline

def main():

    N = int(input())
    A = list(map(int,input().split()))


    wa = defaultdict(int)
    sa = defaultdict(int)

    for i in range(1,N+1):
        wa[i+A[i-1]] +=1
        sa[i-A[i-1]]+=1

    ans = 0
    for j in range(N):
        ans += wa[j] *sa[j]

    print(ans)


if __name__ == "__main__":
    main()