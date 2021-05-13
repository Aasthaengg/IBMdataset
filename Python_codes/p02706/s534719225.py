import sys
import math
def main():
    N,M=tuple(map(int,sys.stdin.readline().split()))
    r=N-sum(tuple(map(int,sys.stdin.readline().split())))
    print('-1') if r<0 else print(r)
if __name__=='__main__':main()