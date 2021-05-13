n = int(input())
ls = [list(map(int,input().split())) for _ in range(n)]
p = 0
for i in range(n):
    j = n-1-i
    q = ls[j][1] - ((ls[j][0]+p)%ls[j][1])
    if q == ls[j][1]:
        q = 0
    p += q
print(p)