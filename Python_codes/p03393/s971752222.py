import sys
def input(): return sys.stdin.readline().strip()
def mapint(): return map(int, input().split())
sys.setrecursionlimit(10**9)

S = list(input())
all_set = set([chr(97+i) for i in range(26)])

if len(S)<26:
    raw_set = set(S)
    lis = list(all_set - raw_set)
    lis.sort()
    S.append(lis[0])
    print(''.join(S))
else:
    can_use = set()
    p = S[-1]
    can_use.add(p)
    for i in range(24, -1, -1):
        nx = S[i]
        if ord(nx)<ord(p):
            for c in sorted(list(can_use)):
                if ord(nx)<ord(c):
                    break
            S = S[:i]+[c]
            print(''.join(S))
            break
        else:
            can_use.add(nx)
            p = nx
    else:
        print(-1)