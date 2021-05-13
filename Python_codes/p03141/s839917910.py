n = int(input())
b_sum = 0
c = []
for _ in range(n):
    a, b = map(int, input().split())
    b_sum += b
    c.append(a + b)
c.sort()
c = list(reversed(c))
print(sum(c[0::2]) - b_sum)