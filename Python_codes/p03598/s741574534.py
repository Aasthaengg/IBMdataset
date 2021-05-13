n = int(input())
k = int(input())
x = list(map(int, input().split()))
t = 0

for i in range(1,n+1):
    k1 = 0
    k2 = 0
    k1 = abs(x[i-1]-0)*2
    k2 = abs(k-x[i-1])*2
    t += min(k1, k2)

print(t)