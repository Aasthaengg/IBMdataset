import sys
input = sys.stdin.buffer.readline
from collections import defaultdict

def main():
    N = int(input())
    a = list(map(int,input().split()))
    d = defaultdict(int)
    ans = 1
    d[0] += 3
    MOD = 1000000007
    for num in a:
        ans *= d[num]
        ans %= MOD
        d[num] -= 1
        d[num+1] += 1
    
    print(ans)

if __name__ == "__main__":
    main()
