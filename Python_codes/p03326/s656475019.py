import sys
input = sys.stdin.buffer.readline
import numpy as np

def main():
    N,M = map(int,input().split())
    point = np.array([list(map(int,input().split())) for _ in range(N)])
    
    ans = 0
    for i in range(2**3):
        pn = np.full(3,1,dtype=int)
        for j in range(3):
            pn[j] = (-1)**(i>>j)
        use = point*pn
        s = np.sum(use,axis=1)
        srev = np.sort(s)[::-1]
        ans = max(ans,np.sum(srev[:M]))
        
    print(int(ans))

if __name__ == "__main__":
    main()
