H,W = map(int,input().split())
h,w = map(int,input().split())
dp = [["W" for i in range(H)] for i in range(W)]
sums = H*W
ans = sums - (h*W+w*H-(h*w))
print(ans)