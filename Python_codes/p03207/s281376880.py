n = int(input())

lis = []
for _ in range(n):
    lis.append(int(input()))
    
lis = sorted(lis)

print(int(max(lis)/2) + sum(lis[:n-1]))