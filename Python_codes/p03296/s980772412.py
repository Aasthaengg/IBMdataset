n = int(input())
li = list(map(int,input().split()))
ans = 0
x = 0

for i in range(1,n):
    if li[i] == li[i-1]:
        x += 1
    else:
        ans += (x+1)//2
        x = 0

ans += (x+1)//2
print(ans)