num = int(input())
a = input().split()
ans = 200
for i in a:
    n = int(i)
    count = 0
    while n%2==0:
        count += 1
        n /= 2
    ans = min(ans, count)

print(ans)