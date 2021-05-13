import bisect,collections,copy,heapq,itertools,math,numpy,string
import sys
sys.setrecursionlimit(10**7)

N = int(input())
S = input()
sl = list(S)
setS = set(S)
ans = 0
for i in range(10):
    if str(i) not in setS:
        continue
    else:
        i100_ind = sl.index(str(i))
        S10 =sl[i100_ind+1:-1]
        S10set = set(S10)
        for j in range(10):
            if str(j) not in S10set:
                continue
            else:
                i10_ind = S10.index(str(j))
                S1 = S10[i10_ind+1:]
                S1.append(sl[-1])
                ans += len(set(S1))
print(ans)
