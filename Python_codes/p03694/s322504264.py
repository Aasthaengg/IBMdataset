import sys
def input(): return sys.stdin.readline().strip()

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    print(A[-1] - A[0])
    

if __name__ == "__main__":
    main()
