import sys
input = sys.stdin.readline
from itertools import product
INF = 10**9
MOD = 10**9 + 7

def main():
    n = int(input())
    a = list(map(int,input().split()))

    bit = 0
    ans = 0
    right = 0
    for left in range(n):
        while right < n:
            num = a[right]
            if num & bit == 0:
                bit += num
                right += 1
            else:
                bit -= a[left]
                break
        ans += right - left
    
    print(ans)
if __name__=='__main__':
    main()