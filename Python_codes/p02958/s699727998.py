N = int(input())
p = list(map(int,input().split()))
s = sorted(p)
cnt = 0
for i in range(N):
    if p[i] != s[i]:
        cnt += 1
        if cnt > 2:
            print('NO')
            exit(0)
print('YES')