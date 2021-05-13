n = int(input())

ls = list(map(int, input().split()))

buff = 1
for i in ls:
    buff *= i

buff -= 1

ans = 0

for i in ls:
    ans += buff % i

print(ans)