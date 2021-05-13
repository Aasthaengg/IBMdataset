n, m = map(int, input().split())
*a, = map(int, input().split())
sorted_a = sorted(a, reverse=True)

needs = [9,2,5,5,4,5,6,3,7,6]
table = [-1] * (n+10)
table[0] = 0

for i in range(n):
    if table[i] != -1:
        for j in sorted_a:
            table[i + needs[j]] = max(table[i]*10 + j, table[i + needs[j]])

print(table[n])