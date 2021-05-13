#n = int(input())
#a, b = map(int,input().split())
#l = list(map(int,input().split()))
#l = [list(map(int,input().split())) for i in range(n)]
s = list(input())
ans = ''
for i, si in enumerate(s):
    if (i+1) % 2 != 0:
        ans += si
print(ans)
