l = list(map(int, input().split()))
k = int(input())
ans = sum(l) - max(l) + max(l)*2**k
print(ans)