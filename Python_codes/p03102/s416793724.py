l = list(map(int, input().split()))
n = l[0]
m = l[1]
c = l[2]

b = list(map(int, input().split()))
a = []
for i in range(n):
    a.append(list(map(int, input().split())))
# a = list(map(int, input().split()) for i in range(n))

num_correct = 0

for i in range(n):
    sum = 0
    for j in range(m):
        sum += a[i][j]*b[j]
    sum += c
    if sum > 0:
        num_correct += 1

print(num_correct)
