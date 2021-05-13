# A - Colorful Slimes 2

N = int(input())
a = list(map(int,input().split()))
ans = 0
tmp = 1

for i in range(1,N):
    if a[i-1]==a[i]:
        tmp += 1
    else:
        tmp = 1
    ans += int(tmp%2==0)

print(ans)