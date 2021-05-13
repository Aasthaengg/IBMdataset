import sys
input = sys.stdin.buffer.readline

def main():
    N = int(input())
    
    ans = 0
    for k in range(10**6):
        k += 1
        if N%k==0:
            i = N//k-1
            if k < i:
                ans += i
                
    print(ans)
    
if __name__ == "__main__":
    main()