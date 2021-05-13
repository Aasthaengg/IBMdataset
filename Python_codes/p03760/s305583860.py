O=list(input())
E=list(input())
ans = ''

for i in range(len(O)):
    ans += O[i]
    if i < len(E):
        ans += E[i]

print(ans)
