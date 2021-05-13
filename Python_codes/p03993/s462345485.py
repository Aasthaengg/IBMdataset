n = int(input())
A = list(map(int, input().split()))

ans = 0
cnt = 0

for a in A:
    cnt += 1
    if A[a-1] == cnt:
        ans += 1

print(ans//2)
