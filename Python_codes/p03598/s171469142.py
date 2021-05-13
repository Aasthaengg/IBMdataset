input()
K = int(input())
ans = 0

for x in map(int, input().split()):
    ans += min(x * 2, abs(K - x) * 2)
    
print(ans)