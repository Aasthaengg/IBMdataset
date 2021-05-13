#k = int(input())
#s = input()
#a, b = map(int, input().split())
#s, t = map(str, input().split())
#l = list(map(int, input().split()))
#l = [list(map(int,input().split())) for i in range(n)]
#a = [list(input()) for _ in range(n)]
#a = [int(input()) for _ in range(n)]

n = int(input())
a = [int(input()) for _ in range(n)]

ans = 0
idx = 0
for i in range(n):
    if (a[idx] == 2):
        break
    else:
        ans += 1
        idx = a[idx] - 1

if (ans == n):
    print(-1)
else:
    print(ans+1)
