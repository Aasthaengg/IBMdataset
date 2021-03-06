import sys
import math
import itertools
import collections
from collections import deque
from collections import defaultdict

sys.setrecursionlimit(1000000)
MOD = 10 ** 9 + 7
MOD2 = 998244353
INF = float('inf')
input = lambda: sys.stdin.readline().strip()

NI = lambda: int(input())
NMI = lambda: map(int, input().split())
NLI = lambda: list(NMI())
SI = lambda: input()

def main():
    S = SI()
    Q = NI()
    
    que = deque(list(S))
    
    reverse = False
    
    for q in range(Q):
        query = input()

        if query == "1":
            if reverse == False:
                reverse = True
            else:
                reverse = False
        else:
            x,y,z = map(str,query.split())
            if reverse == False:
                if y == "1":
                    que.appendleft(z)
                else:
                    que.append(z)
            else:
                if y == "1":
                    que.append(z)
                else:
                    que.appendleft(z)

    if reverse==True:
        print("".join(reversed(list(que))))
    else:
        print("".join(list(que)))#print(x,y,z)



if __name__ == '__main__':
    main()