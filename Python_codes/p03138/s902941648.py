import sys
input = sys.stdin.buffer.readline
import numpy as np

def main():
    N,M = map(int,input().split())
    a = list(map(int,input().split()))
    
    l = max(M,max(a)).bit_length()
    a = np.array(a)
    
    base,ans = 0,0
    for i in reversed(range(l)):
        bit = (a>>i)&1
        c = np.count_nonzero(bit==0)
        if c > N//2:
            if base+2**i <= M:
                base += 2**i
                ans += (2**i)*c
            else:
                ans += (2**i)*(N-c)
        else:
            ans += (2**i)*(N-c)
    
    print(ans)

if __name__ == "__main__":
    main()
