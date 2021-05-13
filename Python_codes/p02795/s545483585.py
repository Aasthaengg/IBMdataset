H = int(input())
W = int(input())
N = int(input())

hi = max(H, W)
print((N+hi-1)//hi)
