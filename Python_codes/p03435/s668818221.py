C = []
for _ in range(3):
    c = list(map(int, input().split()))
    C.append(c)

ans = 'Yes'
for i in range(2):
    d = C[2][i+1] - C[2][i]
    for j in range(2):
        if C[j][i+1] - C[j][i] != d:
            ans = 'No'
print(ans)

