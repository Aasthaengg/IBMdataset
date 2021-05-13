n = int(input())
d = list(map(int, input().split()))

recover = 0

for i in range(n):
    for j in range(n):
        if i==j:
            pass
        else:
            recover += d[i]*d[j]

print(int(recover/2))