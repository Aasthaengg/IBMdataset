n = int(input())
p = list(map(int, input().split()))
l = [i+1 for i in range(n)]
c = 0
for i in range(n):
    if p[i] == l[i]:
        c += 1
print('YES' if c >= n-2 else 'NO')