n = list(map(int,input().split()))
cnt = 0

while n.count(n[0]) != len(n):
    n.sort()
    if n[0] == n[1]:
        n[0] += 1
        n[1] += 1
    else:
        n[0] += 2
    cnt += 1
print(cnt)
