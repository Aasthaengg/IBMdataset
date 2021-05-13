import sys
#import numpy as np
#from collections import defaultdict
import math
#from collections import deque




def main():
    N, K = map(int,input().split())
    R,S,P = map(int,input().split())
    T =  sys.stdin.readline().rstrip()
    tt =[0]*(N+ K)
    ans =0
#    d = deque()
    score = 0
    for i in range(N):
        current = T[i]
        if current == tt[i]:
            pass
        else:
            tt[i + K] = current
            if current == "r":
                ans +=P
            elif current =="s":
                ans +=R
            else:
                ans +=S
 #       print(ans)
    print(ans)





if __name__ == "__main__":
    main()