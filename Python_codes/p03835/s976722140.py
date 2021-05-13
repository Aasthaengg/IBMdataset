k,s=map(int, input().split())
Ans = 0
for i in range(k+1):
    for j in range(k+1):
        x = i
        y = j
        z = s - i - j
        if z <= k and z >= 0:
            Ans += 1
print(Ans)