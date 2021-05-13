n = int(input())
p = list(map(int,input().split()))
l = p
l = sorted(l)
counter = 0 
for i in range(n):
    if p[i] != l[i]: counter += 1
if counter == 2 or counter == 0: print('YES')
else: print('NO')