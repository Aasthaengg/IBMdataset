n = int(input())
p = list(map(int,input().split()))
P = sorted(p)
count = 0
for i in range(n):
    if p[i] == P[i]:
        continue
    else:
        count += 1
print('YES' if count <=2 else 'NO')