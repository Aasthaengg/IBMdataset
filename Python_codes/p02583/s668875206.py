n = int(input())
if n < 3:
    print(0)
    exit()
L = list(map(int,input().split()))
ans = 0
for i in range(n):
    for j in range(i,n):
        for k in range(j,n):
            if L[i] != L[j] and L[i] != L[k] and L[j] != L[k]:
                m = max(L[i],L[j],L[k])
                s = L[i]+L[j]+L[k]
                if m < s-m:
                    ans += 1
print(ans)