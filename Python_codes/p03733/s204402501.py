n, t = map(int, input().split())
T = list(map(int, input().split()))

d = 0
for i in range(n-1):
    d += max(0, t - T[i+1] + T[i])
    
print(n*t - d)