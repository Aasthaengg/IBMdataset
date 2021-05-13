import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
import numpy as np 
def main():
    H, W = map(int, readline().split())
    G = np.zeros((H+2, W+2), np.int16)
    G[1:-1, 1:] = (np.frombuffer(read(H*(W+1)), dtype='B') == ord('.')).reshape((H, W+1))
    def solve(G):
        left = np.zeros(G.shape, np.int16)
        for i in range(G.shape[0]):
            left[i, ] = np.arange(G.shape[1])
        left[G>0] = 0
        np.maximum.accumulate(left, out=left, axis=1)

        rG = G[..., ::-1]
        right = np.zeros(G.shape, np.int16)
        for i in range(G.shape[0]): 
            right[i, ] = np.arange(G.shape[1])
        right[rG>0] = 0
        np.maximum.accumulate(right, out=right, axis=1)

        right = G.shape[1] - right[..., ::-1]-1
        scoreres = (right-left-1) 
        scoreres[G==0] = 0
        return scoreres

    print((solve(G)+solve(G.T).T-1).max())
if __name__ == '__main__':
    main()
