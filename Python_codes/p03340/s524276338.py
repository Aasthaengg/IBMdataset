import sys
input = sys.stdin.buffer.readline

def main():
    N = int(input())
    a = list(map(int,input().split()))
    
    bit = 0
    r = 0
    ans = 0
    for l in range(N):
        while r < N:
            num = a[r]
            if num & bit == 0:
                bit += num
                r += 1
            else:
                num = a[l]
                bit -= num
                break
            ans += r-l
    
    print(ans)
    
if __name__ == "__main__":
    main()
