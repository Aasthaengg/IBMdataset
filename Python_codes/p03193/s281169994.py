N,H,W = map(int,input().split())
AB = [list(map(int,input().split())) for _ in [0]*N]
print(sum(a>=H and b>=W for a,b in AB))
