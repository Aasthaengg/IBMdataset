import math
from typing import List, Any


def read_int() -> int:
    return int(input().strip())


def read_ints() -> List[int]:
    return list(map(int, input().strip().split(' ')))


def solve() -> Any:
    S = input().strip()
    T = input().strip()
    s_t = {}
    t_s = {}
    for s, t in zip(S, T):
        if s not in s_t and t not in t_s:
            s_t[s] = t
            t_s[t] = s
        elif s in s_t and t in t_s:
            if not (s_t[s] == t and t_s[t] == s):
                return 'No'
        else:
            return 'No'
    return 'Yes'



if __name__ == '__main__':
    print(solve())
