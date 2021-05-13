N = int(input())
X = list(map(int, input().split()))
sum_min = 10**8

for i in range(min(X), max(X)+1):
    s = 0
    for j in range(N):
        s += (X[j] - i)**2
    
    if s < sum_min:
        sum_min = s

print(sum_min)