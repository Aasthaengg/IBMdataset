n,c,k = map(int,input().split())
T = sorted([int(input()) for _ in range(n)])
#print(T)
cnt = 0
i = 0
while i < n:
    start = i
    m = 1
    cnt += 1
    while i < n:
        if i - start < c and T[i] - T[start] <= k:
            i += 1
        else:
            break
print(cnt)
