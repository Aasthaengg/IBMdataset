import sys
input = sys.stdin.readline

N = int(input())
p = list(map(int,input().split()))
sort_p= sorted(p)
count = 0
for i in range(N):
    if p[i] != sort_p[i]:
        count += 1
if count <= 2:
    print('YES')
else:
    print('NO')
