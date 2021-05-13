n = [int(s) for s in input().split()]

import datetime

time1 = datetime.datetime(2020,5,5,n[0],n[1])
time2 = datetime.datetime(2020,5,5,n[2],n[3])

time3 = time2 - time1

time3=int(time3.seconds)

result=int(time3/60)
summary = result - n[4]

print(summary)