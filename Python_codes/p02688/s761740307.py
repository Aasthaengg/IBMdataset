n, k = map(int, input().split())
ans = [0] * n
for _ in range(k):
    d = int(input())
    a = list(map(int, input().split()))
    for aa in a:
        ans[aa-1] = 1
cnt = 0
for i in range(n):
    if ans[i] == 0:
        cnt += 1
print(cnt)
