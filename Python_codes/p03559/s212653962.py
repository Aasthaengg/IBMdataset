import bisect
n = int(input())
As = list(map(int, input().split()))
Bs = sorted(list(map(int, input().split())))
Cs = sorted(list(map(int, input().split())))

cnt = [0]*(n+1)
v = 0
for idx, b in enumerate(Bs[::-1]):
    v += len(Cs) - bisect.bisect_right(Cs, b)
    cnt[n-1-idx] = v

print(sum([cnt[bisect.bisect_right(Bs, a)] for a in As]))
