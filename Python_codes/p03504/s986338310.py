N, C = map(int, input().split())
tmp = []

for _ in range(N):
    s, t, c = map(int, input().split())
    tmp.append((s, t, c))
tmp.sort()

# そもそもCが小さいから力技で行けるはず
video = [(0, 0)]  # t,c
for s, t, c in tmp:
    for i, v in enumerate(video):
        ti, ci = v
        if c == ci:
            video[i] = (t, c)
            break
        if s > ti:
            video[i] = (t, c)
            break
    else:
        video.append((t, c))
    video.sort(reverse=True)

ans = len(video)
print(ans)
