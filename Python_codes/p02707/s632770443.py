N = int(input())
an = [int(i) for i in input().split()]

result = { i + 1: 0 for i in range(N) }

for ai in an:
    result[ai] += 1

for r in result.values():
    print(r)
