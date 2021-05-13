n = int(input())
al = list(map(int,input().split()))
al = sorted(al, reverse=True)
ans = 0
for i in range(2*n):
    if i % 2 == 0:
        continue
    ans += al[i]

print(ans)

