import sys
import os

def file_input():
    f = open('AGC009/input.txt', 'r')
    sys.stdin = f

def main():
    #file_input()
    N=int(input())
    A=[]
    B=[]
    for i in range(N):
        tmp=list(map(int, input().split()))
        A.append(tmp[0])
        B.append(tmp[1])

    cnt=0
    for j in range(N):
        # while (A[N-1-j]+cnt)%B[N-1-j]!=0:
        # cnt+=1
        tmp=A[N-1-j]+cnt
        if not tmp==0:
            # cnt=B[N-1-j]
            if tmp<B[N-1-j]:
                cnt+=B[N-1-j]-tmp
            elif tmp%B[N-1-j]!=0:
                cnt+=B[N-1-j]-tmp%B[N-1-j]

    print(cnt)

if __name__ == '__main__':
    main()
