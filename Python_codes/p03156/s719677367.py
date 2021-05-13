n = int(input())
a, b = map(int, input().split())
p = [int(s) for s in input().split()]

count = [0, 0, 0]
for i in range(n):
    if p[i] <= a:
        count[0] += 1
    elif a < p[i] <= b:
        count[1] += 1
    else:
        count[2] += 1
print(min(count))
