import math
minutes = [int(input()) for _ in range(5)]
minutes = sorted(minutes,key = lambda x:-x%10)
cnt = 0
for i in minutes:
    cnt += math.ceil(i/10)*10

if minutes[-1] % 10 !=0:
    cnt -= 10 - minutes[-1] % 10
print(cnt)