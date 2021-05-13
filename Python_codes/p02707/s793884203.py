N = int(input())
A = list(map(int, input().split()))

result = [0] * N

for n in A:
    result[n - 1] += 1

for r in result:
    print(r)
