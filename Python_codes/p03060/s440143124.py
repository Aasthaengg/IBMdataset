import sys
input = sys.stdin.readline
def main():
    N = int(input())
    V = list(map(int, input().split()))
    C = list(map(int, input().split()))
    val = 0
    for i in range(N):
        if V[i]-C[i] >= 0:
            val += V[i]-C[i]
    print(val)

if __name__ == '__main__':
    main()