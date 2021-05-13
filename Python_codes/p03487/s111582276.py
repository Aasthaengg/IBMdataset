n = int(input())
alst = list(map(int, input().split()))
cnt = [0 for _ in range(n)]
for a in alst:
    if a > n:
        continue
    cnt[a - 1] += 1

rem = 0
for i, num in enumerate(cnt, start = 1):
    if num >= i:
        rem += i
        
print(n - rem)