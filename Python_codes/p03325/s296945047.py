N = int(input())
A = list(map(int, input().split()))
ans = 0
for a in A:
    n = a/2
    while n%1 ==0:
        n/=2
        ans += 1
print(ans)