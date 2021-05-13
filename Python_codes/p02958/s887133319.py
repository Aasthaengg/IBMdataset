n = int(input())
l = list(map(int, input().split()))
L = [i for i in range(1, n+1)]
val = 0
for j in range(n):
    if l[j]!=L[j]:
        val += 1
print('YES' if val <3 else 'NO')