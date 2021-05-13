N = int(input())
A = map(int, input().split())
ans = 0

for i in A:
    while i % 2 == 0:
        i /= 2
        ans += 1

print(ans)