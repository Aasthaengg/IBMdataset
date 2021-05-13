N, K = [int(i) for i in input().split()]

ab = [[int(i) for i in input().split()] for _ in range(N)]

length = 0
sorted_ab = sorted(ab, key=lambda x:x[0])

for x in sorted_ab:
    length += x[1]
    if length >= K:
        output = x[0]
        break
    
print(output)