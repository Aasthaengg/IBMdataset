#k = int(input())
a, b, h, m = map(int, input().split())
#al = list(map(int, input().split()))
#al=[list(input()) for i in range(h)]
import math
thetah = 30*h+(m/60)*30
thetam = 6*m
theta=abs(thetah-thetam)
theta=min(theta,360-theta)
ans=math.sqrt(a*a+b*b-2*a*b*math.cos(math.radians(theta)))
print('{:.11f}'.format(ans))
