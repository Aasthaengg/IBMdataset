n = int(input())
p = [int(input()) for _ in range(n)]
id = [0 for _ in range(n)]
for i in range(n):
    id[p[i]-1] = i
cnt = 0
l = r = 0
while l < n:
    while r < n-1 and id[r] < id[r+1]:
        r += 1
    cnt = max(cnt, r-l+1)
    if r == l:
        r += 1
    l = r
print(n-cnt)