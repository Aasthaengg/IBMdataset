import sys
import numpy as np
input = sys.stdin.readline

def main():
    N, K = map(int, input().split())
    A = np.array(list(map(int, input().split())))
    
    ans = 0
    B = np.zeros(40, dtype=int)
    
    for i in range(40):
        B[39-i] = np.count_nonzero(A%2)
        A //= 2
        
    k = 2**39
    x = 0
    for i in range(40):
        if B[i] > N-B[i]: ans += B[i]*k
        else:
            if x+k <= K: x += k; ans += (N-B[i])*k
            else: ans += B[i]*k
        k //= 2
    print(ans)

if __name__ == '__main__':
    main()