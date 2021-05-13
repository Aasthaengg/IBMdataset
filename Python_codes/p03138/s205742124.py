import sys
input = sys.stdin.buffer.readline

def main():
    N,K = map(int,input().split())
    a = list(map(int,input().split()))
    M = max(max(a),K).bit_length()
    l = [0 for _ in range(M)]
    for num in a:
        for i in range(M):
            l[i] += num%2
            num //= 2

    use = 0
    for i in reversed(range(M)):
        if l[i] < -(-N//2):
            if use+2**i <= K:
                use += 2**i
    
    ans = 0        
    for num in a:
        ans += (num^use)
        
    print(ans)

if __name__ == "__main__":
    main()
