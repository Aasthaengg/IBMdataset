O,E = input(),input()
ans = ''

if (len(O)+len(E))%2==0:
    for i in range(len(E)):
        ans += O[i] + E[i]
else:
    for i in range(len(E)):
        ans += O[i] + E[i]
    ans+=O[-1]
    
print(ans)
