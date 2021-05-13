import sys
input = sys.stdin.buffer.readline
import numpy as np

def main():
    N,K = map(int,input().split())
    a = list(map(int,input().split()))
    l = max(max(a),K).bit_length()
    a = np.array(a)
    num,ans = 0,0
    for i in reversed(range(l)):
        base = 2**i
        bit = (a>>i)&1
        cnt = np.count_nonzero(bit)
        
        if cnt <= (N-1)//2:
            if num+base <= K:
                num += base
                ans += base*(N-cnt)
            else:
                ans += base*cnt
        else:
            ans += base*cnt
    
    print(ans)

if __name__ == "__main__":
    main()
