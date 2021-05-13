n = int(input())

if n % 2 == 1:
    print(0)
    exit(0)

div = 10
ans = 0
while n >= div:
    tmp = n
    ans += tmp // div
    div *= 5

print(ans)
