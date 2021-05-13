n = int(input())
x = list(map(int, input().split()))

ans = 0
for i in x:
    ans += 1/i
print(1/ans)