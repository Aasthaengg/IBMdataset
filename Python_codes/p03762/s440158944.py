import sys
input = sys.stdin.buffer.readline

def main():
    N,M = map(int,input().split())
    x = list(map(int,input().split()))
    y = list(map(int,input().split()))
    MOD = 10**9+7
    
    ax,ay = 0,0
    for i,num in enumerate(x):
        ax += num*(i-(N-i-1))
        ax %= MOD
    
    for j,num in enumerate(y):
        ay += num*(j-(M-j-1))
        ay %= MOD
        
    print((ax*ay)%MOD)

if __name__ == "__main__":
    main()
