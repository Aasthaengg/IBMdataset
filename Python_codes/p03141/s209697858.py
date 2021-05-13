n = int(input())
ab = [list(map(int,input().split())) for _ in range(n)]

sum_a = 0
sum_ab = []
for a, b in ab:
    sum_a += a
    sum_ab.append(a + b)

sum_ab.sort(reverse=True)
for i in range(1, n, 2):
    sum_a -= sum_ab[i]
print(sum_a)