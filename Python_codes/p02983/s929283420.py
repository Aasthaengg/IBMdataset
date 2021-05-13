L,R=map(int, input().split())

ans=2100
for i in range(L, L+2019):
    if i>R:
        break
    for j in range(i+1, i+2020):
        if j>R:
            break
        ans=min(ans, (i*j)%2019)

print(ans)