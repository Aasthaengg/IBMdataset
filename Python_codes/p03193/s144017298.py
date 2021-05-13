N,H,W = [int(x) for x in input().split()]
AB = [[int(x) for x in input().split()]for _ in range(N)]
cnt = 0
for a,b in AB:
    if(a>=H and b>=W):
        cnt += 1
print(cnt)