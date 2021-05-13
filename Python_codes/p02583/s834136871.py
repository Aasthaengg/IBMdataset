N = int(input())
l = sorted(list(map(int,input().split())))
ans = 0
for i in range(N):
    for j in range(i,N):
        for k in range(j,N):
            if l[i] != l[j] and l[j] != l[k] and l[k] != l[i]:
                if abs(l[i]-l[j]) < l[k] < l[i] + l[j]:
                    ans += 1
print(ans)
