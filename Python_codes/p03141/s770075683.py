n = int(input())

e = []
curr = 0
for _ in range(n):
    a, b = map(int, input().split())
    e.append(a + b)
    curr -= b

e.sort(reverse=True)
print(curr + sum(e[::2]))
