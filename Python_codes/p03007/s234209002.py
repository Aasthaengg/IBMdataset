import bisect
import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

N = int(input())
L = list(map(int, input().split()))
L = sorted(L)
sum_L = sum(L)
N_neg = bisect.bisect_left(L, 0)
process = []
if N_neg == 0:  # minのみ-にする
    ans = sum_L-min(L)*2
    l = min(L)
    for r in L[1:-1]:
        process.append(str(l)+" "+str(r))
        l -= r
    process.append(str(L[-1])+" "+str(l))
elif N_neg == N:  # maxのみを+にする
    ans = -sum_L+max(L)*2
    l = L[-1]
    for r in reversed(L[:-1]):
        process.append(str(l)+" "+str(r))
        l -= r
else:  # negのやつを-にする
    ans = sum([abs(v) for v in L])
    l = L[0]
    for r in L[N_neg:-1]:
        process.append(str(l)+" "+str(r))
        l -= r
    process.append(str(L[-1])+" "+str(l))
    l = L[-1]-l
    for r in L[1:N_neg]:
        process.append(str(l)+" "+str(r))
        l -= r
print(ans)
print("\n".join(process))
