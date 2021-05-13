import sys
input = sys.stdin.buffer.readline

def main():
    N,M = map(int,input().split())
    a = list(map(int,input().split()))
    cum = 0
    d = {}
    d[0] = 1
    ans = 0
    
    for num in a:
        cum += num
        cum %= M
        if cum not in d:
            d[cum] = 1
        else:
            ans += d[cum]
            d[cum] += 1
        
    print(ans)
        
if __name__ == "__main__":
    main()
