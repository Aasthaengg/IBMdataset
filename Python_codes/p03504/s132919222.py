import sys
from collections import deque
from itertools import accumulate
def input(): return sys.stdin.readline().strip()


def main():
    """
    全部の番組に対して、例えば[2, 4)->[1, 4)のように録画準備時間を確保してたけど、
    同一チャンネルなら、例えば[2, 4), [4, 6)のように続く場合レコーダーは１台で十分。。
    """
    N, C = map(int, input().split())
    channel = [[] for _ in range(C)]
    for _ in range(N):
        s, t, c = map(int, input().split())
        channel[c - 1].append((s, t))
    
    schedule = [0] * (10**5 + 3)
    for c in range(C):
        channel[c].sort()
        channel[c] = deque(channel[c])
        if not channel[c]: continue
        pre_s, pre_t = channel[c].popleft()
        while channel[c]:
            if pre_t == channel[c][0][0]:
                pre_t = channel[c][0][1]
                channel[c].popleft()
                continue
            schedule[pre_s - 1] += 1
            schedule[pre_t] -= 1
            pre_s, pre_t = channel[c].popleft()
        schedule[pre_s - 1] += 1
        schedule[pre_t] -= 1
    total = accumulate(schedule)
    print(max(total))

        
    



if __name__ == "__main__":
    main()
