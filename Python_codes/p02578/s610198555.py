import sys
input = sys.stdin.readline
def main():
    N = int(input())
    A = list(map(int, input().split()))
    CNT = 0
    for i in range(1,N):
        if A[i] <= A[i-1]:
            CNT += A[i-1] - A[i]
            A[i] += A[i-1] - A[i]
    print(CNT)
        

if __name__ == '__main__':
    main()