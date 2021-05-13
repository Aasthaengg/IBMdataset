# S.find()の部分を高速化する
from collections import defaultdict
from bisect import bisect_right
import sys
read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines

def main():
    S = readline().strip()
    T = readline().strip()

    S_idx = defaultdict(list)
    for i, s in enumerate(S):
        S_idx[s].append(i)
    
    rep = 0
    last_idx = -1
    for t in T:
        t_idx_list = S_idx[t]
        if t_idx_list:
            t_idx = bisect_right(t_idx_list, last_idx)
            if t_idx < len(t_idx_list):
                last_idx = t_idx_list[t_idx]
            else:
                last_idx = t_idx_list[0]
                rep += 1
        else:
            print(-1)
            exit()
    
    ans = len(S) * rep + last_idx + 1
    print(ans)


if __name__ == "__main__":
    main()
