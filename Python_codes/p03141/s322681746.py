n = int(input())
ab = [[int(i) for i in input().split()] for j in range(n)]

wa_a_b = []

for i in range(n):
    wa_a_b.append([ab[i][0]+ab[i][1],ab[i][0],ab[i][1]])
    
wa_a_b.sort(reverse=True)

ans = 0

for i in range(n):
    if i % 2 == 0:
        ans += wa_a_b[i][1]
    else:
        ans -= wa_a_b[i][2]
        
print(ans)