import sys
def main():
    input = sys.stdin.readline
    N=int(input())
    *A,=map(int, input().split())
    *B,=map(int, input().split())

    asum=sum(A)
    bsum=sum(B)
    asmall=0
    bsmall=0
    for a,b in zip(A,B):
        asmall+=(max(0, b-a)+1)//2
        bsmall+=max(0, a-b)
    t=bsum-asum
    print('Yes' if t>=max(asmall,bsmall) else 'No')

if __name__ == '__main__':
    main()