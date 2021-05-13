n,c=map(int,input().split())
xv = list(list(map(int, input().split())) for i in range(n))
vx=xv[::-1]
sushi1, max1, sushi2, max2 = [0], [0], [0], [0]
import numpy as np

sum1,sum2=0,0
for x,v in xv:
        sum1+=v
        sushi1.append(max(sum1 - x, sushi1[-1]))
        max1.append(max(sum1 - 2*x, max1[-1]))
for x, v in vx:
    sum2 += v
    sushi2.append(max(sum2 - (c-x), sushi2[-1]))
    max2.append(max(sum2 - 2*(c-x), max2[-1]))
ans1 = max(np.array(sushi1) + np.array(max2[::-1]))
ans2 = max(np.array(sushi2) + np.array(max1[::-1]))
print(max(0, ans1, ans2))