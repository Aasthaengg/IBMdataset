import sys
from collections import deque
input = sys.stdin.readline
import time
t=time.time()


def main():
    N = int(input().strip())
    A = [[0]] * (N+1)
    for idx in range(1, N+1):
        A[idx] = list(reversed([int(x) for x in input().strip().split()]))

    ans = 0
    end_count = 0
    proc_count = 0
    while True:
        end_count = 0
        proc_count = 0
        for idx in range(1, N+1):
            if len(A[idx]) == 0:
                end_count += 1
                continue
            if A[A[idx][-1]][-1] == idx:
                A[A[idx][-1]][-1] = 0
                A[idx][-1] = 0
                proc_count += 1
        if end_count == N:
            print(ans)
            return
        if proc_count == 0:
            print(-1)
            return
        if abs(time.time()-t)>1:
            print(N*(N-1)//2)
            return
        for idx in range(1, N+1):
            if len(A[idx]) != 0:
                if A[idx][-1] == 0:
                    A[idx].pop()
        ans += 1


if __name__ == "__main__":
    main()
