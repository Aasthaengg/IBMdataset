import sys
input = sys.stdin.readline

def main():
    N,M,K = map(int,input().split())
    
    for i in range(N+1):
        for j in range(M+1):
            b = N*M-(i*j+(N-i)*(M-j))
            if b == K:
                print("Yes")
                exit()
    
    print("No")
    
if __name__ == "__main__":
    main()
