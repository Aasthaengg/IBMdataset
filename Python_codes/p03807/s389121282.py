import sys

def main():
    def input(): return sys.stdin.readline().rstrip()
    N = int(input())
    A = list(map(int, input().split()))
    cnt = 0
    for i in range(N):
        if A[i] % 2 != 0:
            cnt += 1
    
    print('YES' if cnt % 2 == 0 else 'NO')
if __name__ == '__main__':
    main()