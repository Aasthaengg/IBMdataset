n, k = map(int, input().split())
A = list(map(int, input().split()))

total = 0

for i in A:
    if i >= k:
        total += 1
        
print(total)