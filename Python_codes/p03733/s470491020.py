n, T = map(int, input().split())
t = [int(x) for x in input().split()]

sum = 0

for i in range(n-1):
    if t[i+1]- t[i] < T:
        sum = sum + t[i+1] - t[i]
    else:
        sum = sum + T

sum = sum + T

print(sum)