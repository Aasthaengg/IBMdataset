n,h,w = map(int,input().split())
abl = [list(map(int,input().split())) for nesya in range(n)]
c = 0
for ab in abl:
  if ab[0] >= h and ab[1] >= w:
    c += 1
print(c)