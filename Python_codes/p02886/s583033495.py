n = int(input())

d = [int(x) for x in input().split()]

result = 0

for i in range(len(d)):
    for h in range(i+1,len(d)):

        result += d[i] * d[h]

print(result)