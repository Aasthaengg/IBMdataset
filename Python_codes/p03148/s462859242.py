#!/usr/bin/env python3
import sys
from collections import defaultdict
from collections import deque


def solve(N: int, K: int, T: "List[int]", D: "List[int]"):
    ml = []

    for t,d in zip(T,D):
        ml.append((t,d))
    ml.sort(key=lambda x: x[1],reverse=True)

    mli = ml[0:K]
    mlo = deque(ml[K:])
    mli.reverse()

    tdic = defaultdict(int)
    for i in mli:
        tdic[i[0]] += 1
    
    max_score = sum(map(lambda x:x[1],mli)) + len(tdic)**2
    prev_score = max_score
    for i,p in enumerate(mli):
        if tdic[p[0]] > 1:
            while len(mlo) > 0:
                q = mlo.popleft()
                if q[0] not in tdic:
                    tdic[p[0]] -= 1
                    tdic[q[0]] += 1
                    mli[i] = q
                    tdic_len  = len(tdic)
                    new_score = prev_score - p[1] + q[1] - (tdic_len-1)**2 + (tdic_len)**2
                    max_score = max(max_score,new_score)
                    prev_score = new_score
                    break

    print(max_score)
    return


# Generated by 1.1.4 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    K = int(next(tokens))  # type: int
    t = [int()] * (N)  # type: "List[int]" 
    d = [int()] * (N)  # type: "List[int]" 
    for i in range(N):
        t[i] = int(next(tokens))
        d[i] = int(next(tokens))
    solve(N, K, t, d)

if __name__ == '__main__':
    main()