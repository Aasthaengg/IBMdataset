H1, M1, H2, M2, K = map(int,input().split())
import math

time1=H1*60+M1
time2=H2*60+M2
a=time2-K
if a<=0:
    print(0)
    exit()

if time1<=a:
    print(a-time1)
else:
    print(0)