n = int(input())
p = list(map(int, input().split()))
lst = []
cnt = 0
for i in range(n - 2):
    lst = [p[i], p[i + 1], p[i + 2]]
    lst.sort()
    if lst[1] == p[i + 1]:
        cnt += 1

print(cnt)