n = int(input())
A = list(map(int, input().split()))

t = 0
for a in A:
    t ^= a
ans = []
for a in A:
    ans += [t ^ a]
    
print(*ans, sep=" ")
