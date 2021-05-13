from collections import defaultdict
H,W,N = map(int,input().split())
d = defaultdict(int)
for i in range(N):
    a,b = map(int,input().split())
    for dy in range(-1,2):
        for dx in range(-1,2):
            if a+dy >= 2 and a+dy <= H-1 and b+dx >= 2 and b+dx <= W-1:
                d[(a+dy,b+dx)] += 1
ans = [0]*10
ans[0] = (H-2)*(W-2)-len(d)
for i in d.values():
    ans[i] += 1
for i in ans:
    print(i)