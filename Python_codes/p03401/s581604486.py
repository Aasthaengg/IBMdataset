N = int(input())
l = list(map(int,input().split()))

l.insert(0, 0)
l.extend([0])
S = 0
ans = 0
for ix, i in enumerate(l[:-1]):
    S += abs(i - l[ix+1])

for ix in range(1,len(l)-1):
    S_i = S - abs(l[ix-1] - l[ix]) - abs(l[ix] - l[ix+1]) + abs(l[ix-1] - l[ix+1])
    print(S_i)