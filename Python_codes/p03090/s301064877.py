N = int(input())
S = N
if N % 2 == 0:
    S += 1
ans = []    
for i in range(1, N+1):
    for j in range(i+1, N+1):
        if i + j == S:
            continue
        ans += [(i, j)]
print(len(ans))
for i, j in ans:
    print(i, j)