n = int(input())
li = list(map(int,input().split()))
x = 0 #まだ未定なら0、単調増加なら1、単調減少なら-1にする
i = 0 #index
ans = 0

if n == 1:
    print(1)
    exit()

while True:
    if x == 0:
        if li[i] < li[i+1]:
            x = 1
        elif li[i] > li[i+1]:
            x = -1
        else:
            x = 0
    if x == 1:
        if li[i] > li[i+1]:
            ans += 1
            x = 0
    if x == -1:
        if li[i] < li[i+1]:
            ans += 1
            x = 0
    i += 1
    if i == n-1:
        break
print(ans+1)