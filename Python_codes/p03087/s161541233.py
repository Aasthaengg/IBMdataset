import sys
import math
 
 
def input():
    return sys.stdin.readline().rstrip()
 
 
def main():
    N, Q = map(int, input().split())
    S = list(input())
    t = [0] * N
    count =0
    for i in range(1,N):
        if S[i-1]=="A" and S[i] =="C":
            count +=1
        t[i] =count
 
    for j in range(Q):
        l, r = map(int,input().split())
        print(t[r-1]-t[l-1])
 
if __name__ == "__main__":
    main()