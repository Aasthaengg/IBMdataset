N = int(input())
p = list(map(int, input().split()))
count = 0
ans = []
for i in range(N):
    if p[i] == i+1:
        if i < N-1 and p[i+1] != i+1:
            p[i], p[i+1] = p[i+1], p[i]
            count += 1
        elif i > 0 and p[i-1] != i:
            p[i-1], p[i] = p[i], p[i-1]
            count += 1
print(count)
            
