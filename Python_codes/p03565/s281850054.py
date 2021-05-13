import math
from typing import List, Any


def read_int() -> int:
    return int(input().strip())


def read_ints() -> List[int]:
    return list(map(int, input().strip().split(' ')))


def solve() -> Any:
    S: str = input().strip()
    T: str = input().strip()
    last_i = -1
    for i in range(len(S)-len(T)+1):
        matches = True
        for t in range(len(T)):
            s = i+t
            if S[s] == '?':
                continue
            elif S[s] != T[t]:
                matches = False
                break
        if matches:
            last_i = i
    if last_i == -1:
        return 'UNRESTORABLE'
    answer = list(S)
    for i in range(last_i, last_i+len(T)):
        answer[i] = T[i-last_i]
    for i in range(len(S)):
        if answer[i] == '?':
            answer[i] = 'a'
    return ''.join(answer)


if __name__ == '__main__':
    print(solve())
