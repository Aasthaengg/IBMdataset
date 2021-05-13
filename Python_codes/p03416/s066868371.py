a,b = map(int,input().split())
cnt = 0
import math

for i in range(a,b+1):
    if i%10 == math.floor(i/10000)%10 and math.floor(i/10)%10 == math.floor(i/1000)%10:
        cnt = cnt + 1
        
print(cnt)