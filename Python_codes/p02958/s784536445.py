n = int(input())
P = list(map(int, input().split()))
sor_P = sorted(P)
count = 0
for i in range(n):
    if P[i] != sor_P[i]:
        count += 1
    if count > 2:
        print('NO')
        exit()
print('YES')
