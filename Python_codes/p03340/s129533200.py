import sys
input = sys.stdin.buffer.readline

def main():
    N = int(input())
    a = list(map(int,input().split()))
    
    le = max(a).bit_length()
    bin = [0 for _ in range(le)]
    l,r = 0,0
    ans = 0
    while r < N:
        num = a[r]
        for i in range(le):
            bin[i] += num%2
            num //= 2
        if 2 not in bin:
            ans += r-l+1
            r += 1
        else:
            while (l < r and 2 in bin):
                num = a[l]
                for i in range(le):
                    bin[i] -= num%2
                    num //= 2
                l += 1
            ans += r-l+1
            r += 1

    print(ans)
    
if __name__ == "__main__":
    main()
