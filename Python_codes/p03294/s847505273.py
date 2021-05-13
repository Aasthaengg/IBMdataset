n = int(input())
A = list(map(int,input().split()))

total = 1
for a in A:
    total *= a

ans = 0
for a in A:
    ans += (total-1) % a

print(ans)