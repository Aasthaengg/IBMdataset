import sys
import math


def input():
    return sys.stdin.readline().rstrip()


def main():
    N, A, B, C, D = map(int, input().split())
    S = input()
    flag = 0
    b=B
    a =A
    while A < C:
        if flag ==1 and S[A]=="#":
            print("No")
            exit()
        elif S[A] =="#":
            flag =1
        else:
            flag =0

        A +=1

    while B < D:
        if flag ==1 and S[B]=="#":
            print("No")
            exit()
        elif S[B] =="#":
            flag =1
        else:
            flag =0

        B +=1

    if C>D:
        j=b-1
        while j<D:
            if S[j-1]=="." and S[j]=="." and S[j+1]==".":
                print("Yes")
                exit()
            j+=1
        print("No")
        exit()
    else:
        print("Yes")




if __name__ == "__main__":
    main()
