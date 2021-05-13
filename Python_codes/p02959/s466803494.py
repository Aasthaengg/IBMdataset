import sys

def I(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def LI(): return list(map(int, sys.stdin.readline().split()))
def main():
    n = I()
    A = LI()
    B = LI()
    ans = 0
    for i in range(n):
        b = B[i]
        a = A[i]
        A[i] = max(0, a-b)
        b = max(0, b-a)
        a = A[i+1]
        A[i+1] = max(0, a-b)
        b = max(0, b-a)
        ans += B[i]-b
    print(ans)

if __name__ == '__main__':
    main()