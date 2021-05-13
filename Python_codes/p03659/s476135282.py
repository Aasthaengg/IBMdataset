n = int(input())
A = list(map(int, input().split()))
total = sum(A)
A.pop()

candidates = []
snuke = 0
for a in A:
    snuke += a
    raccoon = total - snuke
    result = abs(snuke - raccoon)
    candidates.append(result)

print(min(candidates))