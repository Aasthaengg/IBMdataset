n = int(input())
c = {s: 0 for s in 'MARCH'}
for i in range(n):
    s = input()[0]
    if s in 'MARCH':
        c[s]+=1

c = [v for k, v in c.items()]

ans = 0
for i in range(3):
    for j in range(i+1, 4):
        for k in range(j+1, 5):
            ans+=c[i]*c[j]*c[k]
print(ans)