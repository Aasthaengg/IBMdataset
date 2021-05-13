n = int(input())
li = list(map(int,input().split()))
ans = 0

for i in range(n):
    x = li[i]
    if li[x-1] == i+1:
        ans += 1

print(ans//2)