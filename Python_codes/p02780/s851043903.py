n, k = map(int, input().split())
list_P = list(map(int, input().split()))
cnt = 0

for i in range(k):
    p = list_P[i]
    cnt += (1+p)/2

ans = cnt
for i in range(k, n):
    p, q = list_P[i-k], list_P[i]
    cnt -= (1+p)/2
    cnt += (1+q)/2
    ans = max(ans, cnt)

print(ans)