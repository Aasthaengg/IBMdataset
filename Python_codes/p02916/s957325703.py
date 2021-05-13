n = int(input())

a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))

total = 0
p = -1

for i in a:
    total += b[i-1]
    
    if p + 1 == i:
        total += c[i-2]
        
    p = i
    
print(total)