n = int(input())
a = list(map(int, input().split()))
cnt = 0
for i, tgt in enumerate(a, 1):
    if a[tgt - 1] == i:
        cnt += 1
print(cnt // 2)