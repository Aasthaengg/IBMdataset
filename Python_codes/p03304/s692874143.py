import sys
input = sys.stdin.buffer.readline

def main():
    N,M,D = map(int,input().split())
    x = 2*(N-D) if D != 0 else N
    
    print((x*(M-1))/(N**2))
    
if __name__ == "__main__":
    main()