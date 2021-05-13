n = int(input())
ans = 0
for i in map(int,input().split()):
    ans += 1/i
print(1/ans)