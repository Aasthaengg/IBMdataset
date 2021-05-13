N = int(input())
A = map(int, input().split())

k = 1
cnt = 0
for a in A:
    if a == k:
        cnt += 1
        k += 1

ans = -1 if k == 1 else N - cnt
print(ans)
