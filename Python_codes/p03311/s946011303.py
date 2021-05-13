import statistics

N = int(input())
A = list(map(int, input().split()))
A = [a - i for i, a in enumerate(A, 1)]

b = statistics.median(A)
ans = int(sum([abs(a-b) for a in A]))
print(ans)