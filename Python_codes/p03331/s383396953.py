N = int(input())
results = []
for i in range(1, N):
    results.append(sum(map(int, str(i))) + sum(map(int, str(N-i))))
print(min(results))