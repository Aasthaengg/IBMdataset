n = int(input())
p = list(map(int, input().split()))
count = 0
for i in range(1, n-1):
    term3 = p[i-1:i+2]
    if sum(term3) - min(term3) - max(term3) == p[i]:
        count += 1
print(count)
