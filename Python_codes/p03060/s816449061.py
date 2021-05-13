n = int(input())
v = input().split(" ")
c = input().split(" ")

for i in range(n):
    v[i] = int(v[i])
    c[i] = int(c[i])

sum = 0

for i in range(n):
    if(v[i] > c[i]):
        sum += v[i] - c[i]

print(sum)
