n, m = map(int, input().split())
a = list(map(int, input().split()))

needs = [10,2,5,5,4,5,6,3,7,6]
table = [-1] * (n + 10)
table[0] = 0

for i in range(n):
    if table[i] != -1:
        for number in sorted(a, reverse = True):
            matchs = needs[number]
            if table[i+matchs] == 0:
                table[i+matchs] = table[i] * 10 + number
            else:
                table[i+matchs] = max(table[i+matchs], table[i] * 10 + number)

print(table[n])