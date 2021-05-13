n = int(input())
from math import ceil

tkhs = 1
aoki = 1

for _ in range(n):
    t, a = map(int, input().split())
    k = max((tkhs+t-1)//t, (aoki+a-1)//a)
    tkhs = k*t
    aoki = k*a

print(tkhs+aoki)

