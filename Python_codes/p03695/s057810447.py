n = int(input())
alst = list(map(int, input().split()))
lst = [0 for _ in range(9)]
for num in alst:
    pos = min(num // 400, 8)
    lst[pos] += 1
cnt = 8 - lst[:-1].count(0)
print(max(cnt, 1), cnt + lst[-1])