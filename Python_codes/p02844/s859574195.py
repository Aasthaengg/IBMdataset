N = int(input())
S = input()
L = [[] for _ in range(10)]
for i,s in enumerate(S):
    n = int(s)
    L[n].append(i)

count = 0
import bisect
for i in range(1000):
    s = str(i)
    s = s.zfill(3)
    if L[int(s[2])] and L[int(s[0])]:
        r = int(L[int(s[2])][-1])
        l = int(L[int(s[0])][0])
        r2 = bisect.bisect_left(L[int(s[1])], r)
        l2 = bisect.bisect_right(L[int(s[1])], l)
        if r2-l2>0:
            count+=1

print(count)
