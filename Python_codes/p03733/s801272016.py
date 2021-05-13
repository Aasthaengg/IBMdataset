n, T = [int(el) for el in input().split(' ')]
s = [int(el) for el in input().split(' ')]
total = 0
for i in range(n-1):
    total += min(T, s[i+1]-s[i])
print(total + T)
