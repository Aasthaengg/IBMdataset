n = int(input())
rabbit = list(map(int,input().split()))
ans = 0
for i in range(n):
    love = rabbit[i]
    if rabbit[love-1] == i+1:
        ans += 1
print(ans//2)