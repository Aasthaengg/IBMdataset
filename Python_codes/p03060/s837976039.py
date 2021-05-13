N = int(input())
line1 = [int(n) for n in input().split()]
line2 = [int(n) for n in input().split()]
u = []
res = 0
for i in range(N):
    u.append(line1[i]-line2[i])
for i in range(N):
    if u[i]>0:
        res += u[i]
print(res)