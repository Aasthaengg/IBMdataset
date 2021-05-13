n = int(input())
A = list(map(int, input().split()))
d = {}

A.sort()
irregular_cnt=0
reg_cnt = 0
for i in range(n):
    a = A[i]
    a //= 400
    if a>7:
        irregular_cnt += 1
    else:
        d[a] = d.get(a, 0)+1

maxi, mini = 0, 0
for i in d:
    if d[i]>0:
        maxi += 1
        mini += 1
if irregular_cnt:
    maxi += irregular_cnt
    if not mini:
        mini += 1
print(mini, maxi)
