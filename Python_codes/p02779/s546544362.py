n=int(input())
c=sorted(list(map(int, input().split())))
ans = 0

for i in range(n-1):
    if c[i] == c[i+1]:
        ans +=1

if ans == 0:
    print('YES')
if ans != 0:
    print('NO')