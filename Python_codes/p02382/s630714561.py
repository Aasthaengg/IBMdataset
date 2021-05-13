import math
n = int(input())
a1 = list(map(int, input().split()))
a2 = list(map(int, input().split()))
p1, p2, p3, p4 = 0, 0, 0, 0
hyp = 0
for i in range(n):
    p1 += math.fabs(a1[i] -a2[i])
    p2 += (a1[i]-a2[i])**2
    p3 += math.fabs((a1[i]-a2[i])**3)
    hyp = math.fabs(a1[i] -a2[i]) 
    if hyp > p4:
        p4 = hyp

p2 = math.sqrt(p2)
if p3 != 0:
    p3 = math.exp(math.log(p3)/3)
print(p1)
print(p2)
print(p3)
print(p4)