n,x = map(int,input().split())
m = []
count = 0

for _ in range(n):
    m.append(int(input()))

x -= sum(m)

count = n

count += x//min(m)
    
print(count)