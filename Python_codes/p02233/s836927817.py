import sys
input = sys.stdin.readline

def fib2(n):
    n0,n1 = 1,1
    ans = 1
    for i in range(2,n+1):
        n0,n1 = n1,ans
        ans = n0 + n1
    return ans

if __name__ == "__main__":
    n = int(input())
    print(fib2(n))

