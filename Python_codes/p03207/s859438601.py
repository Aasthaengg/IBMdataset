n = int(input())
p = []
for i in range(n):
    p.append(int(input()))
    
p.sort()

print(sum(p) - p[-1] // 2)