import sys
input = sys.stdin.readline

N =int(input())
AB = [list(map(int,input().split())) for _ in range(N)]
ABS = sorted(AB,key = lambda x:x[1])
now = 0
for i in range(N):
    now += ABS[i][0]
    if now > ABS[i][1]:
        print('No')
        exit()
print('Yes')
