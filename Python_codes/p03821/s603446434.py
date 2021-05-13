n = int(input())
ls = []
for i in range(n):
    a,b = map(int, input().split())
    ls.append((a,b))
cnt = 0
for i, j in ls[::-1]:
    m = (i+cnt) % j
    cnt += 0 if m == 0 else (j-m)
print(cnt)