from statistics import median
import math
n = int(input())
a = [int(i) for i in input().split()]
for i in range(n):
    a[i] -= i+1
a_fl = math.floor(median(a))
a_ce = math.ceil(median(a))
ans_fl=ans_ce=0

for i in range(n):
    ans_fl += abs(a[i]-a_fl)
    ans_ce += abs(a[i]-a_ce)
print(int(min(ans_fl,ans_ce)))