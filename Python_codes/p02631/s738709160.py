N = int(input())
A = list(map(int, input().split()))

s = 0
for i in A:
    s ^= i

ans = []
for i in A:
    tmp = s
    tmp ^= i
    ans.append(tmp)
print(*ans)
