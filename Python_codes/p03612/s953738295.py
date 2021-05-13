import sys
input = sys.stdin.readline
def main():
    N = int(input())
    P = list(map(int, input().split()))
    tmp = 0
    CNT = 0
    for i in range(N):
        if P[i] == i+1:
            if i == 0:
                CNT += 1
                tmp = i
            elif i > 1 and tmp != i-1:
                CNT += 1
                tmp = i
            else:
                tmp = 0
    print(CNT)


if __name__ == '__main__':
    main()