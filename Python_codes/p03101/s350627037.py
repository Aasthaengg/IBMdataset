H,W = map(int,input().split(' '))
h,w = map(int,input().split(' '))

ans = H * W
ans1 = H*w
ans2 = W*h
ans = ans - (ans1 + ans2 - (w*h))
print(ans)