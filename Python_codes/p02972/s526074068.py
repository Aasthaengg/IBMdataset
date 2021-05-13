import numpy as np

n = int(input())
A = np.array(list(map(int,input().split())))

balls = np.array([0]*(n+1))

for i in range(1,n+1):
    s = sum(balls[n+1-i::n+1-i])
    if s%2 != A[-i]:
        balls[-i] += 1

#print(balls)

ans = np.where(balls==1)[0].tolist()
if sum(balls):
    print(sum(balls))
    print(*ans)
else:
    print(0)