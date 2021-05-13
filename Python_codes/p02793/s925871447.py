import sys
input = sys.stdin.buffer.readline
from collections import defaultdict

def main():
    N = int(input())
    a = list(map(int,input().split()))
    MOD = 10**9+7
    
    d = defaultdict(int)
    
    for x in a:
        num = x
        count = 0
        while num%2 == 0:
            num //= 2
            count += 1
        d[2] = max(d[2],count)
        for i in range(3,int(x**(1/2))+1,2):
            if num%i == 0:
                count = 0
                while num%i == 0:
                    num //= i
                    count += 1
                d[i] = max(d[i],count)
        if num != 1:
            d[num] = max(d[num],1)

    base = 1
    for x,y in d.items():
        base *= pow(x,y,MOD)
        base %= MOD
        
    s = 0
    for num in a:
        inv_a = pow(num,MOD-2,MOD)
        s += inv_a
        s %= MOD
        
    print((base*s)%MOD)

if __name__ == "__main__":
    main()
