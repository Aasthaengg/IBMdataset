L, R = map(int,input().split())

x = []
for i in range(L,R+1):
    if i % 2019 in x:
        break

    x.append(i % 2019)

ans = 9999
for i in range(len(x)):
    for j in range(i+1,len(x)):
        ans = min(ans, x[i] * x[j] %2019)

print(ans)