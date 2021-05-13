a,b = map(int,input().split())

sabun = b-a

high = 0

for i in range(sabun):
    high += i
    
print(high-a)