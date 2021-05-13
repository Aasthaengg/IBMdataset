import math
n = int(input())
ans = 0
t_1, a_1 = map(int, input().split())
pret = t_1
prea = a_1
for x in range(n - 1):
    t, a = map(int, input().split())
    m = -min(-pret//t,-prea//a)
    pret = m * t
    prea = m * a
print(pret + prea)