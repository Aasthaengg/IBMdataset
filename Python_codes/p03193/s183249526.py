n,h,w = map(int,input().split())
s = [list(map(int,input().split())) for _ in range(n)]
cnt = 0
for a in s:
    if a[0] >= h and a[1] >= w:
        cnt+=1
print(cnt)