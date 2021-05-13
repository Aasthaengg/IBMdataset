n = int(input())
A1 = list(map(int, input().split()))
A2 = list(map(int, input().split()))

ans = 0
for i in range(n):
    s1 = sum(A1[:i+1])
    s2 = sum(A2[i:])
    ans = max(ans, s1 + s2)
print(ans)