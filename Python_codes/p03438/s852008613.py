import sys
input = sys.stdin.readline
def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    CNT = 0
    for i in range(N):
        a = A[i]
        b = B[i]
        if a < b:
            CNT += (b-a+1)// 2
    sa = sum(A)
    sb = sum(B)
    if sa > sb:
        print('No')
    elif sb - sa >= CNT:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()