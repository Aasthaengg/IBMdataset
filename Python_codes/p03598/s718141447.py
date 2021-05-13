N =int(input())
K = int(input())
x = [0]*N
tmp = input().split()
for i in range(N):
    x[i] = int(tmp[i])

d = 0 
for i in range(N):
    d += min(x[i]*2, (K-x[i])*2)

print(d)