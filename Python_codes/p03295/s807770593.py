N, M = map(int,input().split())
AB = []
for _ in range(M):
    t = tuple(map(int,input().split()))
    AB.append(t)
AB.sort()

left = 0
right = N
cnt = 0
for i,(a,b) in enumerate(AB):
    if right <= a:
        cnt += 1
        right = N
        left = 0

    left = max(a,left)
    right = min(b,right)

print(cnt+1)