import numpy as np
from numba import njit

@njit('i8(i8,i8,i8[:],i8[:],i8)', cache=True)
def main(N, K, plist, slist, max_score):
    for start in range(N):

        total_score_in_loop = 0
        score_loop = []
        now = start
        while True:
            now = plist[now]
            total_score_in_loop += slist[now]
            score_loop.append(slist[now])
            if now == start:
                break
        
        rem_score, loop_score = 0, 0
        for idx in range(1, len(score_loop)+1):
            rem_score += score_loop[idx-1]
            if total_score_in_loop > 0:
                loop_score = ((K - idx) // len(score_loop)) * total_score_in_loop
            max_score = max(max_score, rem_score + loop_score)
    return max_score


N, K = map(int, input().split())
plist = np.array([i-1 for i in map(int, input().split())], dtype='int64')
slist = np.array([i for i in map(int, input().split())], dtype='int64')
max_score = -10**15
max_score = main(N, K, plist, slist, max_score)
print(max_score)
