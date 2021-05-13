n = int(input())
a1 = list(map(int,input().split()))
a2 = list(map(int,input().split()))
ans = 0
for i in range(n):
    sum_a1 = sum(a1[:i+1])
    sum_a2 = sum(a2[i:])
    s = sum_a1 + sum_a2
    if s > ans:
        ans = s

print(ans)