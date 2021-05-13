import statistics

results = []
while True:
    n = int(input())
    if n == 0:
        break
    scores = list(map(int, input().split()))
    results.append(statistics.pstdev(scores))

for r in results:
    print(r)
