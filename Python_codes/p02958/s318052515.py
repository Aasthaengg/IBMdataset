import sys
import math

def input():
    return sys.stdin.readline().rstrip()


def main():
    N = int(input())
    P = list(map(int,input().split()))
    PS = sorted(P)
    count =0
    for i in range(N):
        if P[i]!=PS[i]:
            count +=1

    if count==0 or count ==2:
        print("YES")
    else:
        print("NO")



if __name__ == "__main__":
    main()
