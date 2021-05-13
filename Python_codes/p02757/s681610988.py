import sys 
import collections
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
N,P = map(int,readline().split())
S = list(map(int,readline().rstrip().decode()))

def solve_2(S):
    cnt = sum(i for i,x in enumerate(S,1) if x % 2 == 0)
    return cnt
def solve_5(S):
    cnt = sum(i for i,x in enumerate(S,1) if x % 5 == 0)
    return cnt
def solve(S):
    if P == 2:
        return solve_2(S)
    if P == 5:
        return solve_5(S)
    mod_cnt = [0]*(len(S))
    power = 1
    S = S[::-1]
    mod_cnt[0] = S[0] % P
    for i in range(1,len(S)):
        power *= 10
        power %= P
        mod_cnt[i] = (mod_cnt[i-1] + S[i] * power) % P
    c = collections.Counter(mod_cnt)
    cnt = sum( n*(n-1)//2 for n in c.values()) + c[0]
    return cnt

print(solve(S))