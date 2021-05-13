N = int(input())
A = map(int, input().split())
res = [0] * N
for b in A:
    res[b - 1] += 1
for x in res:
    print(x)