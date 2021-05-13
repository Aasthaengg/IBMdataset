n = int(input())
l = [list(map(int,input().split())) for i in range(n)]
ans = 0

for i,j in l[::-1]:
    ans += (j-(i+ans)%j)%j
print(ans)