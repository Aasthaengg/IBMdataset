from collections import defaultdict
import math

def combinations_count(n, r):
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))

def main():
    N = int(input())
    S = defaultdict(int)
    for _ in range(N):
        s = ''.join(sorted(list(input())))
        if s in S:
            S[s] += 1
        else:
            S.update({s:0})
    cnt = 0
    for k,v in S.items():
        if v == 0:
            continue
        elif v == 1:
            cnt += v
        else:
            cnt += combinations_count(v+1,2)
    print(cnt)

if __name__ == '__main__':
    main()