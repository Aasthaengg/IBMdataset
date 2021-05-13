n = int(input())
a = list(map(int, input().split()))
before = 0
ans = 0
for num in a:
    if num == before:
        ans += 1
        before = 0
    else:
        before = num
print(ans)