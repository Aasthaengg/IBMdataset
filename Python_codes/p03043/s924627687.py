n,k = map(int,input().split())

ans = []
n_2 = 1 / n
for i in range(1,n+1):
    c = 0
    while i < k:
        c += 1
        i *= 2
    ans.append(n_2*(0.5**c))

print(sum(ans))
