N=int(input())
P=list(map(int,input().split()))

min = 1e8
n = 0

for i in range(N):
    if P[i] <= min:
        n += 1
        min = P[i]

print(n)