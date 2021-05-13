O=str(input())
E=str(input())
ans=""
for i in range(len(O)):
    ans+=O[i]
    if i<len(E):
        ans+=E[i]
print(ans)