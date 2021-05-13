N, M = map(int, input().split())
ans = 0
for i in map(int,input().split()):
    ans += i

if ans > N:
    print('-1')
else:
    print(N-ans)