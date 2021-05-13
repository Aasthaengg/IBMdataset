n = int(input())

def solve(num):
    cnt = 0
    for i in range(1,num+1):
        if num % i == 0:
            cnt += 1
    return cnt

ans = 0
for i in range(1,n+1):
    if i % 2 == 0:
        continue
    if solve(i) == 8:
        ans += 1

print(ans)

