
N = int(input())
K = int(input())
x = list(map(int, input().split()))
K_half =  K/2

total=0

for i in range(N):
    if K_half>=x[i]:
        total = total + x[i]*2
    else:
        total = total + (K-x[i])*2
print(total)