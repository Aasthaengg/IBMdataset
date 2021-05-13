N, K = map(int,input().split())

if K % 2 == 0:
    ele1 = N // K
    ele2 = (N+K/2) // K
else:
    ele1 = N // K
    ele2 = 0

print(int(ele1**3 +ele2**3))