n = int(input())
l = sorted(list(map(int, input().split())))
ans = 0
ed = []
for i in range(n):
    for j in range(i):
        for k in range(j):
            if (l[k] != l[j] and l[i] != l[j] and l[k] + l[j] > l[i]):ans+=1

print(ans)