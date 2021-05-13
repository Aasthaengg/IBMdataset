n = int(input())
p = [0] + list(map(int,input().split()))
cnt = 0
for i in range(1,n+1):
    if i != p[i]:
        cnt += 1
if cnt in [0,2]:
    print('YES')
else:
    print('NO')