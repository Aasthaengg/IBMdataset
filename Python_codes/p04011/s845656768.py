n = int(input())
k = int(input())

if k > n:
    k = n

a = int(input())
b = int(input())

total = 0

for i in range(1,k+1):
    total += a

for j in range(k,n):
    total += b
    
print(total)