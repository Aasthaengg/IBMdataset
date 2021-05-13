"""
N = list(map(int,input().split()))
S = [str(input()) for _ in range(N)]
S = [list(map(int,list(input()))) for _ in range(h)] 
print(*S,sep="")
"""

import sys
sys.setrecursionlimit(10**6)
input = lambda: sys.stdin.readline().rstrip()
inf = float("inf") # 無限

def main():
    n = int(input())
    if not (n%4) or not(n%7):
        print("Yes")
        return
    for i in range(4,n,4):
        for j in range(7,n,7):
            # print(i,j)
            if n < i+j:
                continue
            elif n == i+j:
                print("Yes")
                return
    print("No")
    return



if __name__ == '__main__':
    main()