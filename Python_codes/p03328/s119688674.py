a, b = map(int, input().split())

t = b - a

total = 0
for i in range(1,t+1):
    total += i
    
print(total - b)