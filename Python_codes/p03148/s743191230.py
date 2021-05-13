import sys
input = sys.stdin.readline

N, K = map(int, input().split())
nums = [[] for i in range(N)]
for i in range(N):
    t, d = map(int, input().split())
    t -= 1
    nums[t].append(d)
maxs = []
rest = []
for i in range(N):
    nums[i].sort(reverse=True)
    if len(nums[i]) > 0:
        maxs.append(nums[i][0])
        for n in nums[i][1:]:
            rest.append(n)
        #rest = rest + nums[i][1:]
maxs.sort(reverse=True)
if len(maxs) > K:
    maxs = maxs[:K]
    for n in maxs[K:]:
        rest.append(n)
    #rest = rest + maxs[K:]
rest.sort(reverse=True)
other = []
idx = 0
while len(maxs)+len(other) < K:
    other.append(rest[idx])
    idx += 1
rest = rest[idx:]

types = len(maxs)
#print(maxs)
#print(rest)
for i,r in enumerate(rest):
    diff = types*types - pow(types-1, 2)
    if diff < r-maxs[len(maxs)-1-i]:
        maxs[len(maxs)-1-i] = r
        types -= 1
    else:
        break
ans = types*types
for num in maxs:
    ans += num
for num in other:
    ans += num
print(ans)
