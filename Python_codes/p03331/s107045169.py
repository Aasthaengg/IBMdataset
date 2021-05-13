n=int(input())

ans = 10000000

for i in range(1,n//2+2):
    memo = 0
    first = str(i)
    second = str(n-i)
    for j in first:
        memo += int(j)
    for j in second:
        memo += int(j)
    ans = min(memo,ans)

print(ans)