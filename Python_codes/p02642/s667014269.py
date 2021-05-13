n = int(input())
a = sorted([int(_) for _ in input().split(' ')])
a.append(0)

d = set()
answer = 0

for i in range(n):
    if not(a[i] in d):
        if a[i] != a[i + 1]:
            answer += 1
        for j in range(a[i], 1000001, a[i]):
            d.add(j)

print(answer)
